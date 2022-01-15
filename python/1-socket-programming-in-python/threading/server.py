#!/usr/bin/env python3

import os
import socket
from _thread import *

ServerSocket = socket.socket()
host = ""
port = 8889
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waiting for a connection..")
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode("Welcome to Server\n"))
    while True:
        data = connection.recv(2048)
        reply = "Server Says:" + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))

    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print("Connected to:" + address[0] + ":" + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    print("Thread Number:" + str(ThreadCount))
    ThreadCount = ThreadCount + 1

    ServerSocket.close()
