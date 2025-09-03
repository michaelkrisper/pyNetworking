#!/usr/bin/python3
# coding=utf-8
"""A simple TCP server that listens for a connection, receives data,
converts it to uppercase, and sends it back to the client.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket

def handle_connection(conn, addr):
    """Handles a single client connection."""
    print("Connection from : {}".format(addr))
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            data = data.decode()
            print("from connected user: {}".format(data))
            data = data.upper()

            print("sending: {}".format(data))
            conn.send(data.encode())
    finally:
        conn.close()

def main():
    """Sets up the server socket, listens for a connection, and handles it."""
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

    print("Server started.")
    conn, addr = s.accept()
    handle_connection(conn, addr)
    s.close()


if __name__ == "__main__":
    main()