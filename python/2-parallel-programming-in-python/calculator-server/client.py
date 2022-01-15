#!/usr/bin/env python3

import socket
import sys

ClientSocket = socket.socket()
host = "127.0.0.1"
port = 8888

print("Waiting for connection")
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input(
        "Choose mathematical function, [L]ogarithmic, [S]quare Root, or [E]xponential. Enter only the first capital letter or [Q] to quit: "
    )

    if Input == "L" or Input == "S" or Input == "E":
        value = input("Enter a value: ")
        Input = Input + ":" + value

        ClientSocket.send(str.encode(Input))
    elif Input == "Q":
        print("Quiting app.")
        ClientSocket.send(str.encode(Input))
        sys.exit()
    else:
        print("Invalid input! Enter only L, S, or E.")
        sys.exit()

    Response = ClientSocket.recv(1024)
    print(Response.decode("utf-8"))

    ClientSocket.close()
