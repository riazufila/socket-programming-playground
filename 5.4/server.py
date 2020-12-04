#!/usr/bin/env python3

import socket

s = socket.socket()
PORT = 4545
s.bind(('', PORT))
s.listen(10)

file = open("got-hello.txt", "wb")

while True:
    conn, addr = s.accept()
    msg = "Message from server"
    conn.send(msg.encode("utf-8"))
    data = conn.recv(1024)

file.close()
conn.close()
