#!/usr/bin/env python3

import socket
from cryptography.fernet import Fernet


if __name__ == '__main__':
    # variables declaration
    port = 17  # Default QOTD port
    ip_host = b"192.168.12.34"  # Server's ip
    msg = b"Let me in!"
    sym_key = b'db81nHBk-RcQ_-zSMcWdCEuH53LUX1PFiCA_2R7CKK8='

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send datagram to Server for QOTD
    s.sendto(msg, (ip_host, port))

    # Receive datagram from Server
    data, addr = s.recvfrom(512)  # 512 bytes as recommended in RFC

    # Decrypt the message with the defined key
    en_type = Fernet(sym_key)
    de_msg = en_type.decrypt(data)

    # Print out the quote
    print("QOTD: %s" % (data.decode("utf-8")))
