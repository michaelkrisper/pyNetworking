import socket
import unittest
import threading
import time
from tcpServer import main as tcp_server_main
from tcpClient import send_message as tcp_send_message
from udpServer import main as udp_server_main
from udpClient import send_message as udp_send_message

class TestSocketExamples(unittest.TestCase):

    def setUp(self):
        self.tcp_server_stop_event = threading.Event()
        self.udp_server_stop_event = threading.Event()

        self.tcp_server_thread = threading.Thread(target=self.run_tcp_server)
        self.udp_server_thread = threading.Thread(target=self.run_udp_server)

        self.tcp_server_thread.daemon = True
        self.udp_server_thread.daemon = True

        self.tcp_server_thread.start()
        self.udp_server_thread.start()
        time.sleep(1)

    def tearDown(self):
        self.tcp_server_stop_event.set()
        self.udp_server_stop_event.set()

        # Send a dummy message to unblock the udp server
        try:
            with socket.socket(type=socket.SOCK_DGRAM) as s:
                s.sendto(b'', ("127.0.0.1", 5000))
        except Exception as e:
            print(f"Error sending dummy message to UDP server: {e}")

        # Connect to tcp server to unblock it
        try:
            with socket.socket() as s:
                s.connect(("127.0.0.1", 5000))
        except Exception as e:
            print(f"Error connecting to TCP server to unblock: {e}")


        self.tcp_server_thread.join(timeout=2)
        self.udp_server_thread.join(timeout=2)


    def run_tcp_server(self):
        host = "127.0.0.1"
        port = 5000
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        s.settimeout(1)
        while not self.tcp_server_stop_event.is_set():
            try:
                conn, addr = s.accept()
                from tcpServer import handle_connection
                handle_connection(conn, addr)
            except socket.timeout:
                continue
        s.close()

    def run_udp_server(self):
        host = "127.0.0.1"
        port = 5000
        s = socket.socket(type=socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.settimeout(1)
        from udpServer import handle_message
        while not self.udp_server_stop_event.is_set():
            try:
                handle_message(s)
            except socket.timeout:
                continue
        s.close()

    def test_tcp(self):
        with socket.socket() as s:
            s.connect(("127.0.0.1", 5000))
            response = tcp_send_message(s, "hello")
            self.assertEqual(response, "HELLO")

    def test_udp(self):
        with socket.socket(type=socket.SOCK_DGRAM) as s:
            s.bind(("127.0.0.1", 5001))
            response = udp_send_message(s, ("127.0.0.1", 5000), "world")
            self.assertEqual(response, "WORLD")

if __name__ == '__main__':
    unittest.main()
