# Author: Dionne Bang
# Date: 12/7/22
# Description: Server side of a simple client-server multiplayer tic-tac-toe ascii game.
# Citation for following program:
# Date retrieved: 12/5/22
# Source code based on: Kurose and Ross, Computer Networking: A Top-Down Approach, 7th Edition,Pearson, Chapter 2.7

from socket import *
import pickle

serverPort = 56565

# The server creates a socket and binds to ‘localhost’ and port xxxx
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))

# The server then listens for a connection
serverSocket.listen(1)

print('Waiting for message...')
connectionSocket, addr = serverSocket.accept()

# When connected, the server calls recv to receive game invite
invite = connectionSocket.recv(1024).decode()

# The server prints invite, then prompts for answer
print(invite)
reply = input('>')
connectionSocket.send(reply.encode())

while reply.lower() != 'y':
    # if server doesn't want to play
    if reply.lower() == 'n':
        print('Okay, bye!')
        connectionSocket.close()
        break

    # if server types something other than y/n
    elif reply.lower() != 'y' and reply.lower() != 'n':
        reply = input('Invalid answer! Type \'Y\' or \'N\': ')
        connectionSocket.send(reply.encode())

if reply.lower() == 'y':
    # if server wants to play
    print('Let\'s play!')
    print('Waiting for first move...')

    while True:
        # receive board from client
        game = connectionSocket.recv(1024)
        updatedGame = pickle.loads(game)
        updatedGame.print_board()

        # close if game over
        if updatedGame.get_game_state() == 'GAME OVER':
            print(updatedGame.get_game_result())
            print(updatedGame.get_game_state())
            connectionSocket.close()
            break

        # play if game ongoing
        # server makes move
        myMove = input('Your move: ')
        updatedGame.make_move(myMove)

        while updatedGame.get_move_validity() == False:
            myMove = input('Your move: ')
            updatedGame.make_move(myMove)

        # send client updated game
        sendGame = pickle.dumps(updatedGame)
        connectionSocket.send(sendGame)

        # close if game over
        if updatedGame.get_game_state() == 'GAME OVER':
            print(updatedGame.get_game_state())
            connectionSocket.close()
            break

        print('Their move.')
