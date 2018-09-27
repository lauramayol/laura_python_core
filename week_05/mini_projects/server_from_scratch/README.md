$Inventory Project
========

Inventory Project takes API calls to display and modify current inventory.

PATH
--------

    localhost:8000/inventory

QUERY VARIABLES
--------

- item: the item name currently in inventory.
- quant: quantity to be added/removed from inventory. Must be paired with item.
- confirm_delete: Must be included with DELETE method with value = 1 to confirm you want to remove the item from invenvtory. Must have at least one item specified in query.

SEE CURRENT INVENTORY
--------

Method: GET
Variables:
- item (optional)

To get current inventory list use GET method:

    localhost:8000/inventory

To only view specific items, use query:

    localhost:8000/inventory?item=socks&item=pants

Add new item
--------

Method: POST
Variables:
- item
- quant (optional, default = 0)
    - Note: quantity must be listed for all items in order. It is all or nothing, specify quantity for all items, or omit for all.

To add an item to inventory list use POST method:

    localhost:8000/inventory?item=socks&quant=2

You can also add multiple items at once, such as:

    localhost:8000/inventory?item=socks&quant=2&item=scarves&quant=10



Update quantity in inventory (incremental)
------------

Method: PUT
Variables:
- item
- quant
    - Note: quantity must be listed for all items in order. It is all or nothing, specify quantity for all items, or omit for all.

Syntax is same as "add new item", but only updates quantities for existing item specified. The quantity listed is the incremental amount (remove units by specifying negative 'quant').

Update quantity in inventory (overwrite)
------------

Method: PATCH
Variables:
- item
- quant (optional, default = 0)
    - Note: quantity must be listed for all items in order. It is all or nothing, specify quantity for all items, or omit for all.

Syntax is same as "add new item", but only updates quantities for existing item specified. The quantity listed is the amount to replace existing (overwrite).

Eliminate item from iventory
------------

Method: DELETE
Variables:
- item

Delete one or multiple items at once. Must specify "confirm_delete=True", otherwise delete will be ignored.

    localhost:8000/inventory?item=socks&confirm_delete=True
