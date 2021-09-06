#!/usr/bin/env python3

import socket
import sys

import PySimpleGUI as sg
from cryptography.fernet import Fernet

if __name__ == "__main__":
    # variables declaration
    port = 17  # Default QOTD port
    ip_host = b"192.168.12.34"  # Server's ip
    msg = b"Let me in!"
    sym_key = b"db81nHBk-RcQ_-zSMcWdCEuH53LUX1PFiCA_2R7CKK8="

    # Window's layout
    sg.theme("Dark Blue 9")
    layout = [
        [sg.Text("Do you want to receive the quote of the day?")],
        [sg.Button("Yes"), sg.Button("No")],
    ]

    # Window creation
    window = sg.Window("Question of the Day", layout)

    # Interact with the window
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "No":
            sys.exit()

        if event == "Yes":
            break

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
    print("QOTD: %s" % (de_msg.decode("utf-8")))

    # Window's layout
    quote_size = len(de_msg)
    counter = 1

    while quote_size >= 50:
        if quote_size == 50:
            counter = 1
            break
        else:
            while quote_size > 50:
                quote_size = quote_size % 50
                counter = counter + 1

    layout = [[sg.Text(size=(50, counter), key="-OUTPUT-")], [sg.Button("Quit")]]

    # Window creation
    window = sg.Window("Quote of the Day", layout, finalize=True)

    # Interact with the window
    window["-OUTPUT-"].update(de_msg.decode("utf-8"))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Quit":
            sys.exit()
