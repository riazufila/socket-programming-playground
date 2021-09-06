#!/usr/bin/env python3

import socket

s = socket.socket()
print("Managed to create the socket!")

port = 8888

s.bind(("", port))
print("Binded the socket at port:" + str(port))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Received connection from:" + str(addr))

    c.send(b'Thank you.')
    buffer = c.recv(1024)
    print(buffer)

    c.close()
