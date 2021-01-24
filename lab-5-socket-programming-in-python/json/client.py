#!/usr/bin/env python3

import socket
import sys
import json

s = socket.socket()

port = 8080

s.connect(("192.168.42.198", port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client')

dataJ = json.loads(data)

print(type(dataJ))
print(dataJ)

s.close()
