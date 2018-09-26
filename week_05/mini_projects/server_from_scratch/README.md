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

GET
--------

To get current inventory list use GET method:

    localhost:8000/inventory

To only view specific items, use query:

    localhost:8000/inventory?item=socks&item=pants

POST
--------

To add an item to inventory list use POST method:

    localhost:8000/inventory?item=socks&quant=2

Note that the quantity (quant) is optional. If not listed, the default value is 0. You can also add multiple items at once, such as:

    localhost:8000/inventory?item=socks&quant=2&item=scarves&quant=10

Please note that quantity must be listed for all items in order. It is all or nothing, specify quantity for all items, or omit for all.

PUT
------------

Similart to POST method, but only to update quantities for an existing item. The quantity listed is the incremental amount (you can remove units by using negative 'quant').

PATCH
------------

Similart to POST method, but only to update quantities for an existing item. The quantity listed is the new amount to replace existing (not incremental).

DELETE
------------

Delete one or multiple items at once. Must specify "confirm_delete=True", otherwise delete will be ignored. Quantity is ignored here as well, the full item will be removed from inventory as long as it is confirmed.

    localhost:8000/inventory?item=socks&confirm_delete=1
