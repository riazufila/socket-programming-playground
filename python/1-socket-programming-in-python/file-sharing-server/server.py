#!/usr/bin/env python3

import socket

from Crypto.Cipher import AES  # Library for encryption


# Decryption
def decrypt(encrypted_data):
    obj = AES.new(b"1234567890123456", AES.MODE_CFB, b"0987654321098765")
    data = obj.decrypt(encrypted_data)

    return data


s = socket.socket()  # Socket creation
PORT = 4545  # Port defined
s.bind(("", PORT))  # Binding socket
s.listen(10)  # Socket waits for connections

while True:
    conn, addr = s.accept()

    filename = conn.recv(1024)
    file = open(filename, "wb")

    msg = "Message from server"
    conn.send(msg.encode("utf-8"))

    RecvData = conn.recv(1024)
    RecvData = decrypt(RecvData)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)
        RecvData = decrypt(RecvData)

    file.close()
    conn.close()
    break
