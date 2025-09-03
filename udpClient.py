#!/usr/bin/python3
# coding=utf-8
"""A simple UDP client that sends messages from user input to a server and
prints the server's response.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket

def send_message(sock, server_address, message):
    """Sends a single message to the server and returns the response."""
    sock.sendto(message.encode(), server_address)
    data, _ = sock.recvfrom(1024)
    return data.decode()

def main():
    """Binds the client socket and sends messages to the server."""
    host = "127.0.0.1"
    port = 5001
    server = ("127.0.0.1", 5000)

    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind((host, port))

    try:
        message = input("Enter a message: ")
        while message:
            response = send_message(s, server, message)
            print("Received from server: {}".format(response))
            message = input("Enter a message: ")
    finally:
        s.close()


if __name__ == "__main__":
    main()