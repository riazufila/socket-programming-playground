#!/usr/bin/env python3

import os
import socket
from Crypto.Cipher import AES


def encryption(data):
    obj = AES.new(b"1234567890123456", AES.MODE_CFB, b"0987654321098765")
    encrypted_data = obj.encrypt(data)

    return encrypted_data


IP = "192.168.42.198"
PORT = 4545
FILE = input("Enter the absolute path for the file to send to serve: ")
FILESIZE = os.path.getsize(FILE)

s = socket.socket()
s.connect((IP, PORT))

file = open(FILE, "rb")
SendData = file.read(1024)

length = 16 - (len(SendData) % 16)
SendData += bytes([length])*length

SendData = encryption(SendData)

while SendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)
    SendData = encryption(SendData)

s.close()
