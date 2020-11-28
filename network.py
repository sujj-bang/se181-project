import socket
import pickle


class Network:
    def __init__(self):
        self.main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.main.connect(self.addr)
            return self.main.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            self.main.send(str.encode(data))
            return pickle.loads(self.main.recv(4096))
        except socket.error as e:
            print(e)

