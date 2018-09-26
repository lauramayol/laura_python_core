import json
import sys
from inventory_exception import InventoryException


class MyApp:
    # Set class attributes
    inventory_file = 'inventory_api.txt'
    item_str = 'item'
    quantity_str = 'quant'
    confirm_dlt_str = 'confirm_delete'
    default_quantity = 0
    exc_status = '400 Bad Request'

    def dispatch(self, environ):
        # Get details of HTTP request
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        # read your current inventory based on inventory_file variable
        item_list = self.filereader()
        # First we parse the query into a dictionary.
        split_query = self.read_query(query)
        # Currently, we only handle requests within inventory path.
        if path == '/inventory':
            if method == 'GET':
                inven = self.get_inventory(split_query, item_list)
                # dumps returns a json formatted string of our inventory.
                return json.dumps(inven)
            # Other methods except GET will require query values to be introduced. And item_str must be part of the query.
            elif self.item_str in split_query:
                return self.inventory_workflow(method, split_query, item_list)
        return 'Your request is invalid, please try new URL'

    def filewriter(self, fileinfo):
        json.dump(fileinfo, open(self.inventory_file, 'w'))
        return 'Your inventory has been updated'

    def filereader(self):
        _dict = {}
        with open(self.inventory_file, 'r') as f:
            _dict = json.loads(f.read())
        return _dict

    def read_query(self, query_str):
        '''
            Break up the query into a dictionary. Each individual field being queried becomes a key (separated by & in original)
            --The values for each key are a list, so you can have multiple items queried at once. The corresponding values (ie. quantities), will then be assigned by matching indexes.
            --While quantity is not required (default is 0), it is all or nothing. If quantity is listed for one item, it must be listed for all of them.

            Example: ?item=socks&quant=2&item=pants&quant=1
            Result: {item : [socks, pants], quant : [2, 1]}
        '''

        query_dict = {}
        if len(query_str) > 0:
            for stmt in query_str.split("&"):
                # The values (separated by =) become a list value of that key.
                stmt_list = stmt.split("=")

                if stmt_list[0] in query_dict:
                    query_dict[stmt_list[0]].append(stmt_list[1])
                else:
                    query_dict[stmt_list[0]] = [stmt_list[1]]
            new_query_dict = self.check_quantities(query_dict)
            return new_query_dict
        return query_dict

    def check_quantities(self, _dict):
        '''
        Check if the query includes item and quantity specifications. If it includes quantity, every item should have one. Otherwise, it should be a separate request.
        '''
        if self.item_str in _dict and self.quantity_str in _dict:
            # Make sure that every item has a quantity spec. Otherwise raise exception.
            if len(_dict[self.item_str]) != len(_dict[self.quantity_str]):
                raise InventoryException("Your request is invalid. Include quantity for all items, or remove all quantities to use default.", self.exc_status)
        return _dict

    def inventory_workflow(self, method, query_dict, data_list):
        if method == 'DELETE':
            new_data_list = self.delete_inventory(query_dict, data_list)
        else:
            new_data_list = self.iterate_query(method, query_dict, data_list)

        post_update = self.filewriter(new_data_list)
        return_dict = {"message": post_update, "inventory": new_data_list}
        return_message = json.dumps(return_dict)
        return return_message

    def iterate_query(self, method, _dict, _list):
        # Iterate through the items given in the request query
        new_data_list = dict()
        for i, val in enumerate(_dict[self.item_str]):
            # Assign quantity from split_query dictionary based on index value matching the item location.
            if self.quantity_str in _dict:
                try:
                    q = int(_dict[self.quantity_str][i])
                except:
                    raise InventoryException(f"Quantity ({self.quantity_str}) expected integer. Instead it recieved {_dict[self.quantity_str][i]}", self.exc_status)
            else:
                q = self.default_quantity
            new_data_list = self.change_inventory(method, _list, val, q)
        return new_data_list

    def change_inventory(self, request_type, _dict, item, num):
        '''
        If the request is PATCH or PUT, the "num" amount will be added to quantity. Removing units requires a negative number so it is also "added."
        '''
        if item in _dict and request_type == 'PUT':
            _dict[item] += num
        # If the request is "POST", a new item will be created with quantity "num"
        elif (item not in _dict and request_type == 'POST') or request_type == 'PATCH':
            _dict[item] = num
        else:
            raise InventoryException("Your request is invalid, please try new URL", self.exc_status)
        return _dict

    def get_inventory(self, query_dict, data_list):
        new_data_list = dict()
        if len(query_dict) == 0:
            new_data_list = data_list

        # All other methods will require query values to be introduced.
        # Check if the query is requesting "item"
        elif self.item_str in query_dict:
            # Iterate through the items given in the request query
            for i, val in enumerate(query_dict[self.item_str]):
                if method == 'GET':
                    new_data_list[val] = data_list[val]
        return new_data_list

    def delete_inventory(self, query_dict, inventory_list):
        '''
        Can only fully remote items if you "confirm_delete". Also, all items in this DELETE method will be deleted as long as "confirm_delete" = 1 is found once.
        '''
        for i, val in enumerate(query_dict[self.item_str]):
            if 'True' in query_dict[self.confirm_dlt_str]:
                del inventory_list[val]
            else:
                raise InventoryException(f"Your request is invalid. DELETE request should include {confirm_dlt_str}=True. Please try new URL.", self.exc_status)
        return inventory_list
