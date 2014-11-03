#!/usr/bin/python3
# coding=utf-8
"""
TcpServer
https://www.youtube.com/watch?v=XiVVYfgDolU
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket


def main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    conn, addr = s.accept()
    print("Connection from : {}".format(addr))

    while True:
        data = conn.recv(1024)
        if not data:
            break

        print("from connected user: {}".format(data))
        data = str(data).upper()

        print("sending: {}".format(data))
        conn.send(data)
    conn.close()


if __name__ == "__main__":
    main()