import random
gameover = 0  # Keeps track whether game has finished
mode = 0  # Whether AI is X or O
move = 1  # Move Counter for AI
played = 0

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']         # Display Board
myboard = [5, 5, 5, 5, 5, 5, 5, 5, 5]       # Internal Calculation board

def display(PlayerTurn):
    print('- indicates blank spaces\n\n')
    print(board[1], '|', board[2], '|', board[3])
    print('-' * 10)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 10)
    print(board[7], '|', board[8], '|', board[9])

    if PlayerTurn == 1:       # It is player's turn
        print('Your Move\n')
        choice = int(input('Choose a spot'))
        while board[choice] != '-':
            print('As you can see, that spot is already taken mate')
            choice = int(input('Choose a spot'))
    # After receiving proper input
        if mode == 0:
            board[choice] = 'O'
            myboard[choice] = 2
            display(0)     # Send 0 as it is AI's turn now
        if mode == 1:
            board[choice] = 'X'
            myboard[choice] = 3
            display(0)  # Send 0 as it is AI's turn now


display(0)

def modex():
    if move == 1:
        board[5] = 'X'
        myboard[5] = 3
        display(1)


mode = random.randint(0,1)
if mode == 0:
    print('Computer plays X and goes first\n\n')
    modex()
else:
    print('Computer plays O and goes second\n\n')
    # modeo()









def checkwin():
    r1 = myboard[1]*myboard[2]*myboard[3]
    r2 = myboard[4]*myboard[5]*myboard[6]
    r3 = myboard[7]*myboard[8]*myboard[9]
    c1 = myboard[1]*myboard[4]*myboard[7]
    c2 = myboard[2]*myboard[5]*myboard[8]
    c3 = myboard[3]*myboard[6]*myboard[9]
    d1 = myboard[1]*myboard[5]*myboard[9]
    d2 = myboard[3]*myboard[5]*myboard[7]

    if r1||r2||r3||c1||c2||c3||d1||d2 == 45:   #Wow
        if r1||r2||r3 == 45:
            if r1 == 45:
                for i in range(1,3):
                    if myboard[i] == 5:
                        display(0,i)     #It is AI's turn and must fill position i
            if r2 == 45:
                for i in range(4, 6):
                    if myboard[i] == 5:
                        display(0, i)  # It is AI's turn and must fill position i
            if r3 == 45:
                for i in range(7, 9):
                    if myboard[i] == 5:
                        display(0, i)  # It is AI's turn and must fill position i










