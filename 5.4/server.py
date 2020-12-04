#!/usr/bin/env python3

import socket
from Crypto.Cipher import AES


def decrypt(encrypted_data):
    obj = AES.new(b"1234567890123456", AES.MODE_CFB, b"0987654321098765")
    data = obj.decrypt(encrypted_data)

    return data


s = socket.socket()
PORT = 4545
s.bind(('', PORT))
s.listen(10)

file = open("got-hello.txt", "wb")

while True:
    conn, addr = s.accept()
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
