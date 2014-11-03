#!/usr/bin/python3
# coding=utf-8
"""
https://www.youtube.com/watch?v=XiVVYfgDolU#t=1344
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"


import socket

def main():
    host = "127.0.0.1"
    port = 5001

    server = ("127.0.0.1", 5000)

    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind((host, port))
    try:
        message = input("Enter a message: ")
        while message:
            s.sendto(message.encode(), server)
            data, addr = s.recvfrom(1024)
            data = data.decode()
            print("Received from server: {}".format(data))
            message = input("Enter a message: ")

    finally:
        s.sendto(b"", server)
        s.close()


if __name__ == "__main__":
    main()