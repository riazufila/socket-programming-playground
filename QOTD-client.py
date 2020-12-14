#!/usr/bin/env python3

import socket


if __name__ == '__main__':
    # variables declaration
    port = 17  # Default QOTD port
    ip_host = b"192.168.12.34"  # Server's ip
    msg = b"Let me in!"

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send datagram to Server for QOTD
    s.sendto(msg, (ip_host, port))

    # Receive datagram from Server
    data, addr = s.recvfrom(512)  # 512 bytes as recommended in RFC
    print("QOTD: %s" % (data.decode("utf-8")))
