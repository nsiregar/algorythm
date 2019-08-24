from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from socket import socket

HOST, PORT = '', 3000
PACKET_SIZE = 1024

listener = socket(AF_INET, SOCK_STREAM)
listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
listener.bind((HOST, PORT))
listener.listen(1)
print(f'Serving HTTP on port {PORT}')

while True:
    client_conn, client_addr = listener.accept()
    request = client_conn.recv(PACKET_SIZE)
    print(request.decode('utf-8'))

    response = b"""\
HTTP/1.1 200 OK

Response !!!!
"""

    client_conn.sendall(response)
    client_conn.close()
