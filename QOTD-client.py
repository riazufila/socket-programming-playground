#!/usr/bin/env python

import socket


def main():
    PORT = 17  # Default QOTD port
    IP = b"192.168.42.69"  # Server's IP
    MSG = b"Let me in!"

    # Create socket
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send datagram to Server for QOTD
    SOCKET.sendto(MSG, (IP, PORT))

    # Receive datagram from Server
    data, addr = SOCKET.recvfrom(512)  # 512 bytes as recommended in RFC
    print("QOTD: %s" % (data.decode("utf-8")))


if __name__ == '__main__':
    main()
