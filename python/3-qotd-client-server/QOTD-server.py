#!/usr/bin/env python3

import socket
import threading
from datetime import datetime

from cryptography.fernet import Fernet


def encrypt_msg(MSG):
    # Encrypt with predefined key
    sym_key = b"db81nHBk-RcQ_-zSMcWdCEuH53LUX1PFiCA_2R7CKK8="
    en_type = Fernet(sym_key)
    en_msg = en_type.encrypt(MSG)

    return en_msg


def send_msg(SOCKET, MSG, addr):
    SOCKET.sendto(MSG, addr)
    print("Sent Quote to %s" % (str(addr[0])))


def get_quote(day):
    f = open("quotes.txt", "r")

    day_buffer = datetime.now()
    day_differences = day_buffer - day
    day_differences = str(day_differences)
    day_differences = day_differences.split(" ")[0]
    day_diff_len = len(day_differences)
    MSG = ""

    if day_diff_len == 1:
        MSG = f.readline().encode("utf-8")
    else:
        i = int(day_differences[0])
        for x in range(i + 1):
            MSG = f.readline().encode("utf-8")

    return MSG


if __name__ == "__main__":

    # Variables declaration
    PORT = 17  # Set default port for QOTD

    # Create socket and bind
    try:
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as socket_error:
        print("Socket failed to create with error %s" % (socket_error))

    try:
        SOCKET.bind(("", PORT))
    except socket.error as socket_error:
        print("Socket failed to bind with error %s" % (socket_error))

    # Socket listening
    while SOCKET:
        # Check for new day
        day = datetime.now()

        try:
            print("Ready to receive connections..")

            # based on RFC for QOTD Protocol the size must not exceed 512 bytes
            # Data received is discarded
            data, addr = SOCKET.recvfrom(512)

            print("Connection established from %s" % str(addr[0]))
        except socket.error as socket_error:
            print("Socket failed to receive data with error %s" % (socket_error))

        try:
            # Get QOTD
            MSG = get_quote(day)

            # Encrypt message with fernet
            MSG = encrypt_msg(MSG)

            # Send quote to client
            # Threading to allow multiple clients at the same time
            threading.Thread(target=send_msg, args=(SOCKET, MSG, addr)).start()
        except socket.error as socket_error:

            print("Socket failed to send data with error %s" % (socket_error))
