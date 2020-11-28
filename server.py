import socket
from _thread import *
from checkers.game import Game
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

connected = set()
games = {}
idNum = 0


def threaded_player(conn, p, gameID):
    global idNum
    conn.send(str.encode(str(p)))
    reply = ""

    while True:
        try:
            data = conn.recv(4096).decode()
            if gameID in games:
                game = games[gameID]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        pos = str.split(",")
                        game.select(int(pos[0]), int(pos[1]))
                        game.change_turn(p)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Connection Stopped")
    try:
        del games[gameID]
        print("Closing Game ", gameID)
    except:
        pass
    idNum -= 1
    conn.clos()


while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    idNum += 1
    p = 0
    gameID = (idNum - 1) // 2

    if idNum % 2 == 1:
        games[gameID] = Game(gameID)
        print("Creating a new game, waiting for another player to join...")
    else:
        games[gameID].ready = True
        p = 1

    start_new_thread(threaded_player, (conn, p, gameID))
