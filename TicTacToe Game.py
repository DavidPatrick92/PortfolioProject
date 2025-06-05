#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initial game setup
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
Player = "X"
winner = None
gameRunning = True

# Function to print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to handle player input
def playerInput(board):
    inp = int(input(f"Player {Player}, enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp-1] == "-":
        board[inp-1] = Player
    else:
        print("Invalid move! Try again.")
        playerInput(board)

# Win and tie checks
def checkColumn(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkWin():
    return checkColumn(board) or checkRow(board) or checkDiagonal(board)

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def switchPlayer():
    global Player
    Player = "0" if Player == "X" else "X"

def play_game():
    # These are reset at the start of every game
    global board, Player, winner, gameRunning
    board = ["-"] * 9
    Player = "X"
    winner = None
    gameRunning = True

    while gameRunning:
        printBoard(board)
        playerInput(board)
        if checkWin():
            printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False
            break
        checkTie(board)
        if not gameRunning:
            break
        switchPlayer()

# Main loop to allow replay
while True:
    play_game()
    again = input("Play again? (Y/N): ").upper()
    if again != "Y":
        print("Thanks for playing!")
        break


# In[ ]:




