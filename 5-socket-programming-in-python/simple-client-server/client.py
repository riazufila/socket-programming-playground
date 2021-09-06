#!/usr/bin/env python3

import socket

s = socket.socket()

port = 8888

s.connect(('192.168.8.112', port))

data = s.recv(1024)

s.send(b'Hello, I am the client!')

print(data)

s.close()
