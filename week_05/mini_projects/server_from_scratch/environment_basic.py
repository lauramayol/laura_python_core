# Python's bundled WSGI server
from wsgiref.simple_server import make_server

# set the encoding
encoding = 'utf-8'
# set port
port = 8000
ip_address = 'localhost'


def application(environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body.encode(encoding)]


# Instantiate the server
httpd = make_server(
    ip_address,  # The host name
    port,  # A port number where to wait for the request
    application  # The application object name, in this case a function
)

print(f"Serving application on {port}...")

# Wait for a single request, serve it and quit
httpd.serve_forever()
