import socket
from _thread import *
import sys
import pickle

server = "10.0.0.209"  # server ip address to be added
port = 5555  # used a port number that is not used to anything

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server Started, Waiting for Connection")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""  # soon to be changed to checkers object instead of string

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received : ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Stopped")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (conn,))
