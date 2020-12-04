#!/usr/bin/env python3

import os
import socket

IP = "192.168.42.198"
PORT = 4545
FILE = "hello.txt"
FILESIZE = os.path.getsize(FILE)

s = socket.socket()
s.connect((IP, PORT))

s.send("Hello server!")

file = open(FILE, "rb")
SendData = file.read(1024)

while SendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)

s.close()
