# @Author Jose Daniel Acuna
# Last time edited 10/12/19
# Reference https://pymotw.com/2/socket/tcp.html

import socket


class Server:

    def __init__(self):
        self.Ip = socket.gethostbyname(socket.gethostname())
        self.port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = (self.Ip, 10000)
        print("Server starting %s:%d" % (self.Ip, self.port))
        self.sock.bind(server_address)

    def listen(self):
        self.sock.listen(10)
        while True:
            print("Server waiting connection...")
            connection, client_address = self.sock.accept()
            message = self.read(connection, client_address)
            self.send(connection, message)
            connection.close()

    @staticmethod
    def read(connection, client_address):
        print("Client connected %s", client_address)
        message = ""
        try:
            while True:
                data = connection.recv(16)
                if data:
                    message += data.decode()
                else:
                    break
        finally:
            print("Server receive: %s", message)
            return message

    @staticmethod
    def send(connection, response):
        print("Server sending: %s", response)
        connection.send(response.encode())


server = Server()
server.listen()
