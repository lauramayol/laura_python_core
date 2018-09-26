# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from wsgiref.util import guess_scheme
import json
import inventory
from inventory_exception import InventoryException

# set the encoding
encoding = 'utf-8'
# set port
port = 8000
# create object of MyApp
my_obj = inventory.MyApp()


def application_(environ, start_response):

    try:
        response_text = my_obj.dispatch(environ)
    except InventoryException as ie:
        response_text = ie.__str__()
    except Exception as exc:
        print(exc)
        status = '500 Internal Server Error'
        response_text = ''
    status = '200 OK'  # HTTP Status
    headers = [
        ('Content-Type', 'text/plain; charset=' + encoding),  # HTTP Headers
        #        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, headers)

    return [response_text.encode(encoding)]


# Instantiate the server
httpd = make_server(
    '',  # The host name
    port,  # A port number where to wait for the request
    application_  # The application object name, in this case a function
)

print(f"Serving application on {port}...")

# Wait for a single request, serve it and quit
httpd.serve_forever()
