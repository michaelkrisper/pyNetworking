#!/usr/bin/python3
# coding=utf-8
"""
https://www.youtube.com/watch?v=XiVVYfgDolU#t=1079
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket


def main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(type=socket.SOCK_DGRAM)

    s.bind((host, port))

    try:
        print("Server started")

        while True:
            data, addr = s.recvfrom(1024)

            if not data:
                break

            data = data.decode()
            print("Message from {}".format(addr))
            print("from connected user: {}".format(data))

            data = data.upper()

            print("Sending: {}".format(data))

            s.sendto(data.encode(), addr)

    finally:

        s.close()

if __name__ == "__main__":
    main()