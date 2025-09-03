#!/usr/bin/python3
# coding=utf-8
"""A simple UDP server that listens for messages, converts them to
uppercase, and sends them back to the client.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket

def handle_message(s):
    """Receives and handles a single message."""
    data, addr = s.recvfrom(1024)
    if not data:
        return False

    data = data.decode()
    print("Message from {}".format(addr))
    print("from connected user: {}".format(data))

    data = data.upper()

    print("Sending: {}".format(data))
    s.sendto(data.encode(), addr)
    return True

def main():
    """Sets up the server socket and handles incoming messages."""
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(type=socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    print("Server started")
    try:
        while handle_message(s):
            pass
    finally:
        s.close()


if __name__ == "__main__":
    main()