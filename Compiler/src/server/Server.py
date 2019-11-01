# @Author Jose Daniel Acuna
# Last time edited 10/12/19
# Reference https://pymotw.com/2/socket/tcp.html
#           https://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/

import socket
import sys
import time


class Server:

    def __init__(self):
        self.Ip = 'localhost'
        self.port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        server_address = (self.Ip, self.port)
        print("Server starting %s:%d" % server_address)
        self.sock.bind(server_address)
        self.listen()

    def listen(self):
        self.sock.listen(10)
        while True:
            print("Server waiting connection...")
            try:
                connection, client_address = self.sock.accept()
                message = self.read(connection, client_address)
                self.send(connection, message)
                connection.close()
            except:
                e = sys.exc_info()[0]
                print("Server interrupted")
                print("<p>Error: %s</p>" % e)
                break

    @staticmethod
    def read(connection, client_address, timeout=1):
        print("Client connected %s:%d" % client_address)
        connection.setblocking(0)
        total_data = []
        begin = time.time()

        while True:
            # If you got some data, then break after timeout
            if total_data and (time.time() - begin) > timeout:
                break

            # Recv data
            try:
                data = connection.recv(16).decode()
                if data:
                    total_data.append(data)
                    begin = time.time()
            except:
                pass

        # Converts the final message to a string
        message = ''.join(total_data)
        print("Server receive: %s" % message)
        return message

    @staticmethod
    def send(connection, response):
        print("Server sending: %s" % response)
        connection.send(response.encode())
