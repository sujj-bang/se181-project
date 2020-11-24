import socket
import pickle


class Network:
    def __init__(self):
        self.main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.209"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.main.connect(self.addr)
            return self.main.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.main.send(str.encode(data))
            return self.main.recv(2048).decode()
        except socket.error as e:
            print(e)

