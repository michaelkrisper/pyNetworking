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
        s.close()


if __name__ == "__main__":
    main()