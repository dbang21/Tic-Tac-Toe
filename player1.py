# Author: Dionne Bang
# Date: 12/7/22
# Description: Client side of a simple client-server multiplayer tic-tac-toe ascii game.
# Citation for following program:
# Date retrieved: 12/5/22
# Source code based on: Kurose and Ross, Computer Networking: A Top-Down Approach, 7th Edition,Pearson, Chapter 2.7

from socket import *
from tictactoe import *
import pickle

serverName = 'localhost'
serverPort = 56565

# The client creates a socket and connects to ‘localhost’ and port xxxx
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Let's play Tic Tac Toe!")
print("Inviting other player...")
invite = "Do you want to play Tic Tac Toe? (Y/N)"
clientSocket.send(invite.encode())
reply = clientSocket.recv(1024)
reply = reply.decode().lower()

while True:
    # Socket closes if server refuses invite.
    if reply == 'n':
        print('Invite rejected! Goodbye.')
        clientSocket.close()

    elif reply == 'y':
        print('Invite accepted! Let\'s play!')
        newGame = TicTacToe()
        newGame.print_board()

        while True:
            myMove = input('Your move: ')
            newGame.make_move(myMove)
            while newGame.get_move_validity() == False:
                myMove = input('Your move: ')
                newGame.make_move(myMove)

            # send server updated game
            sendGame = pickle.dumps(newGame)
            clientSocket.send(sendGame)

            # if game over, close connection
            if newGame.get_game_state() == 'GAME OVER':
                print(newGame.get_game_state())
                clientSocket.close()
                break

            # receive server's move
            print('Their move.')
            theirMove = clientSocket.recv(1024)
            newGame = pickle.loads(theirMove)
            newGame.print_board()

            # if game over, close connection
            if newGame.get_game_state() == 'GAME OVER':
                print(newGame.get_game_result())
                print(newGame.get_game_state())
                clientSocket.close()
                break
        break

    else:
        reply = clientSocket.recv(1024)
        reply = reply.decode().lower()
