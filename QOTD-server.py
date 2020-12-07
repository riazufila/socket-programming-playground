#!/usr/bin/env python

import socket
from multiprocessing import Pool
from datetime import datetime


def main():
    PORT = 17  # Set default port for QOTD

    # Create socket
    try:
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as socket_error:
        print("Socket failed to create with error %s" % (socket_error))

    # Bind socket
    try:
        SOCKET.bind(('', PORT))
    except socket.error as socket_error:
        print("Socket failed to bind with error %s" % (socket_error))

    while SOCKET:
        # Check for new day
        day = datetime.now()

        try:
            print("Ready to receive connections..")
            # based on RFC for QOTD Protocol the size must not exceed 512 bytes
            data, addr = SOCKET.recvfrom(512)
            print("Connection established from %s" % str(addr[0]))
            # Data received is discarded
        except socket.error as socket_error:
            print("Socket failed to receive data with error %s" % (socket_error))

        try:
            # Get QOTD
            f = open("quotes.txt", "r")

            day_buffer = datetime.now()
            day_differences = day_buffer - day
            day_differences = str(day_differences)
            day_differences = day_differences.split(" ")[0]
            day_diff_len = len(day_differences)

            if day_diff_len == 1:
                MSG = f.readline().encode("utf-8")
            else:
                i = int(day_differences[0])
                for x in range(i + 1):
                    MSG = f.readline().encode("utf-8")

            # Send QOTD to client
            SOCKET.sendto(MSG, addr)
            print("Sent Quote to %s" % (str(addr[0])))
        except socket.error as socket_error:
            print("Socket failed to send data with error %s" % (socket_error))


if __name__ == '__main__':
    main()
