#!/usr/bin/env python3

import socket

ClientSocket = socket.socket()
host = '192.168.8.112'
port = 8889

print("Waiting for a Connection")
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input("Say something:")
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode("utf-8"))

    ClientSocket.close()
