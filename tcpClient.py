#!/usr/bin/python3
# coding=utf-8
"""
TcpClient
https://www.youtube.com/watch?v=XiVVYfgDolU#t=646
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import socket

def main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("Enter a message: ")
    try:
        while message:
            s.send(message.encode())
            data = s.recv(1024).decode()
            print("Received from server: {}".format(data))
            message = input("Enter a message: ")
    finally:
        s.close()


if __name__ == "__main__":
    main()