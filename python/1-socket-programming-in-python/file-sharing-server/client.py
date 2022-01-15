#!/usr/bin/env python3

import os
import socket

from Crypto.Cipher import AES  # Encryption module

# Encryption process


def encryption(data):
    obj = AES.new(b"1234567890123456", AES.MODE_CFB, b"0987654321098765")
    encrypted_data = obj.encrypt(data)

    return encrypted_data


IP = "192.168.42.198"
PORT = 4545
FILE = input("Enter the filename (must be in the same directory) to send to server: ")
FILESIZE = os.path.getsize(FILE)

# Socket creation
s = socket.socket()
# Socket connection
s.connect((IP, PORT))

file = open(FILE, "rb")
SendData = file.read(1024)

# Sending filename to server
s.send(FILE.encode("utf-8"))

# Padding
length = 16 - (len(SendData) % 16)
SendData += bytes([length]) * length

SendData = encryption(SendData)

while SendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)
    SendData = encryption(SendData)

    s.close()
