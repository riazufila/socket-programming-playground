#!/usr/bin/env python3

import socket
import sys
import json

mydata = {"id": 505012, "name": "Azizi", "age": "29"}
sendData = json.dumps(mydata)

s = socket.socket()
print("SockeT successfully created")

port = 8080

s.bind(('', port))
print("Socket binded to " + str(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from" + str(addr))

    c.sendall(bytes(sendData.encoding("utf-8")))
    buffer = c.recv(1024)
    print(buffer)

c.close()
