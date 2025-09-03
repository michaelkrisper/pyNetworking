#!/usr/bin/python3
# coding=utf-8
"""A simple TCP client that connects to a server, sends messages from user
input, and prints the server's response.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket

def send_message(sock, message):
    """Sends a single message to the server and returns the response."""
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    return data

def main():
    """Connects to the server and sends messages."""
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("Enter a message: ")
    try:
        while message:
            response = send_message(s, message)
            print("Received from server: {}".format(response))
            message = input("Enter a message: ")
    finally:
        s.close()


if __name__ == "__main__":
    main()