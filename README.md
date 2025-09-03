# Python Networking Examples

This repository contains simple examples of TCP and UDP clients and servers implemented in Python 3.

## Description

The scripts demonstrate basic socket programming for both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

*   **TCP Server (`tcpServer.py`)**: Listens for a TCP connection on `localhost:5000`. When a client connects, it receives data, converts it to uppercase, and sends it back.
*   **TCP Client (`tcpClient.py`)**: Connects to the TCP server, sends messages entered by the user, and prints the server's uppercase response.
*   **UDP Server (`udpServer.py`)**: Listens for UDP datagrams on `localhost:5000`. When a message is received, it converts it to uppercase and sends it back to the source address.
*   **UDP Client (`udpClient.py`)**: Sends UDP datagrams containing user-entered messages to the UDP server on `localhost:5000` and prints the server's uppercase response.

## How to Run

You will need two terminal windows to run the client and server pairs.

### TCP Example

1.  **Start the server:**
    ```bash
    python3 tcpServer.py
    ```

2.  **In a new terminal, start the client:**
    ```bash
    python3 tcpClient.py
    ```
    You can now type messages in the client terminal and see the server's response.

### UDP Example

1.  **Start the server:**
    ```bash
    python3 udpServer.py
    ```

2.  **In a new terminal, start the client:**
    ```bash
    python3 udpClient.py
    ```
    You can now type messages in the client terminal and see the server's response.
