#!/usr/bin/env python

import socket


def main():
    """Main function"""
    # variables declaration
    port = 17  # Default QOTD port
    ip_host = b"192.168.42.69"  # Server's ip
    msg = b"Let me in!"

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send datagram to Server for QOTD
    s.sendto(msg, (ip_host, port))

    # Receive datagram from Server
    data, addr = s.recvfrom(512)  # 512 bytes as recommended in RFC
    print("QOTD: %s" % (data.decode("utf-8")))


if __name__ == '__main__':
    main()
