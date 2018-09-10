'''
Build a small web server following the first part of the tutorial at:
https://ruslanspivak.com/lsbaws-part1/

'''

import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()

'''
    Below is the code I ran on the command line (it works!)

Lauras-Air:~ lauramay$ cd CodingNomads/Python\ testing/
Lauras-Air:Python testing lauramay$ ls
Repl quizzes.py intro_4.py  intro_6.py
intro.py    intro_5.py  webserver1.py
Lauras-Air:Python testing lauramay$ python webserver1.py

Lauras-Air:~ lauramay$ nc localhost 8888
GET /hello HTTP/1.1
HTTP/1.1 200 OK

Hello, World!
Lauras-Air:~ lauramay$
'''
