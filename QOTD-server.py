#!/usr/bin/env python

import socket

PORT = 17  # Set default port for QOTD
MSG = b"The world is ending.."

# Create socket
try:
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as socket_error:
    print("Socket failed to create with error %s" % (socket_error))

# Bind socket
try:
    SOCKET.bind(('', PORT))
except socket.error as socket_error:
    print("Socket failed to bind with error %s" % (socket_error))

while SOCKET:
    print("Ready to receive connections..")
    # based on RFC for QOTD Protocol the size must not exceed 512 bytes
    data, addr = SOCKET.recvfrom(512)
    print("Connection established from %s" % str(addr[0]))
    # Data received is discarded
    # Send QOTD to client
    SOCKET.sendto(MSG, addr)
