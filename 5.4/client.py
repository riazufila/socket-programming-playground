#!/usr/bin/env python3

import os
import socket

IP = "192.168.42.198"
PORT = 4545
FILE = input("Enter the absolute path for the file to send to serve: ")
FILESIZE = os.path.getsize(FILE)

s = socket.socket()
s.connect((IP, PORT))

file = open(FILE, "rb")
SendData = file.read(1024)

while SendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)

s.close()
