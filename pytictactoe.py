import random

def display_board(b):
    print('\n'*100)
    print('╔═══╦═══╦═══╗')
    print('║ ' + b[7] + ' ║ ' + b[8] + ' ║ ' + b[9] + ' ║')
    print('╠═══╬═══╬═══╣')
    print('║ ' + b[4] + ' ║ ' + b[5] + ' ║ ' + b[6] + ' ║')
    print('╠═══╬═══╬═══╣')
    print('║ ' + b[1] + ' ║ ' + b[2] + ' ║ ' + b[3] + ' ║')
    print('╚═══╩═══╩═══╝')

def player_input():
    player1 = None
    while player1 not in ['X', 'O']:
        player1 = input("Please pick a marker (X/O): ").upper()
        if player1 not in ['X', 'O']:
            print("Invalid input. Please pick either X or O.")
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):    
     return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] == board[5] == board[6] == mark) or # across the middle
    (board[1] == board[2] == board[3] == mark) or # across the bottom
    (board[7] == board[4] == board[1] == mark) or # down the middle
    (board[8] == board[5] == board[2] == mark) or # down the middle
    (board[9] == board[6] == board[3] == mark) or # down the right side
    (board[7] == board[5] == board[3] == mark) or # diagonal
    (board[9] == board[5] == board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    
def player_choice(board,turn):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{turn}, choose your next position: (1-9) '))        
    return position

def replay():    
    return input('Do you want to play again? Y/N: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Y/N: ') 
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(f'Congratulations, {turn}! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(f'Congratulations, {turn}! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break