import socket
from _thread import *
from checkers import game
from checkers.board import Board
from checkers.constants import RED, WHITE
import sys
import pickle

server = "localhost"  # server ip address to be added
port = 5555  # used a port number that is not used to anything

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server Started, Waiting for Connection")

# connected = set()

connected = 0
p = 0
turn = RED
array = Board()


def threaded_player(conn, p):
    global connected
    global turn
    global array
    conn.send(str.encode(str(p)))

    reply = ""

    while True:
        try:

            data = pickle.loads(conn.recv(4096))

            print(data)

            # game = Game()

            if not data:
                break
            else:

                if isinstance(data, str) == False:
                    array = data

                    conn.sendall(pickle.dumps(0))

                if data == "giveMe":
                    conn.sendall(pickle.dumps(array))
                if data == "connected":
                    conn.sendall(pickle.dumps(connected))

                if data == "turn":
                    conn.sendall(pickle.dumps(turn))
                if data == "changeTurn":
                    if turn == RED:
                        turn = WHITE
                    elif turn == WHITE:
                        turn = RED
                    conn.sendall(pickle.dumps(0))

        except EOFError as e:
            print(e)
            break

    print("Connection Stopped")
    try:
        del game
        print("Closing Game ")
    except:
        pass
    # idNum -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    connected += 1
    p += 1

    print("Creating a new game, waiting for another player to join...")

    start_new_thread(threaded_player, (conn, p))
