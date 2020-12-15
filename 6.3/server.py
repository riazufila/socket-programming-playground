#!/usr/bin/env python3

import math
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found\n\n'


def process_start(s_sock):
    s_sock.send(str.encode("Welcome to the Server\n"))
    while True:
        data = s_sock.recv(2048).decode("utf-8").split(":")

        if data[0] == "L":
            result = math.log(data[1])
        elif data[0] == "S":
            result = math.sqrt(data[1])
        elif data[0] == "E":
            result = math.exp(data[1])
        else:
            break

        s_sock.sendall(str.encode(result))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8888))
    print("Listening...")
    s.listen(3)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()
            except socket.error:
                print("Got a socket error.")
    except Exception as e:
        print("An exception occured!")
        print(e)
