from random import randrange

    # A function EVALUATE that accepts the string with the board, and returns one character based on the state of the game
def evaluate (string):
    if 'xxx' in string:
        return 'x'
    elif '000' in string:
        return '0'
    elif not '-' in string:
        return '!'
    else:
        return '-'


    # A function PRINT_RESULT, prints the end messages 
def print_result(board):
    result = evaluate(board)
    print(board)
    if result == 'x':
        return 'You won'
    elif result == '0':
        return 'The mighty computer won!'
    elif result == '!':
        return "Nobody won!"
    else:
        return 'Hmm, how exactly you came here!'
    
    # A MOVE function that accepts the string with the game board, a position number (0-19) and a (x or 0) mark 
    #and returns a game board (i.e., a string with the given mark placed in the given position).
def move(board, mark, position):
    new_board = board[:position] + mark + board[position + 1:]
    return new_board


'''Write a PLAYER_MOVE function that accepts a string with the game board, asks the player 
which position he wants to play and returns board with the player's move. 
The function should reject negative or too large numbers or moves to an occupied position. 
If the user has entered a wrong argument, the function should ask again (to get correct answer).
The IS_VALID_COICE function is to check if a given position is empty
'''
def is_valid_choice (board, position):
    
    return board[position] == '-'
       
    
def player_move(board):
    print('This is the current situation on the board:')
    print(board)
    
    while True:
        try:
           position = int( input('On which possition would you like to play (number between 0 and 19 )'))
        except ValueError:
            print('Are you sure you gave us a correct number between 0 and 19 and that the chosen space is free to play!')
            continue
        if position <= 19 and position >= 0 and is_valid_choice (board, position):
            new_board = move(board,'x', position)
            return new_board
        else: 
            print('Are you sure you gave us a correct number between 0 and 19 and that the chosen space is free to play!')
        
    
         



def pc_strategy_move(board):
    strategy_dict = { '-00': 0, '00-': 2, '0-0': 1,  # winning moves
                     'x-x': 1, '-xx': 0, 'xx-': 2,   # prevent opponent from winning
                     '--0-': 1, '-0--': 2,           # secure win on next move
                     '-0-': 0,                       # play next to previous move
                     '--x-': 1, '-x--': 2,           # prevent opponent from win in two moves
                     '-x': 0, 'x-': 1,               # prevent opponent from putting next to a move
                     '---': 1, '--': 0, '-': 0 }     # play on a free spot,
    #but with this strategy the player never has a chance of winning this game , the maximum is 
    for key, value in strategy_dict.items():
        position = board.find(key)
        print(key, value, position)
        if position != -1:
            print(position + value)
            return position + value
        
         

   
    # A PC_MOVE function accepts the game board. It will select a position to play, 
    #  and returns the game board with the computer's move.           

def pc_move(board):
    
    # commented out snippet is the pc_move with randoomly chosen spot
    # pc_choice_local = randrange(0, 19)

    # while not is_valid_choice(board, pc_choice_local):
    #     pc_choice_local = randrange(0,19)
    
    pc_choice_local = pc_strategy_move(board)
    print(pc_choice_local)
    return move(board,'0', pc_choice_local)
    


    # TICTACTOE_GAME function creates a string with a game board 
    # and alternately calls the player_move and pc_move functions until someone wins or draws

def tictactoe_game():
    board = '-'
    for i in range(19):
        board += '-'
    print(board)
    while True:
        result = evaluate(board)
        if result != '-':
            return print_result(board)
        else:
            board = player_move(board)
            result = evaluate(board)
            if result != '-':
                return print_result(board)
            else:
                board = pc_move(board)
                
        


print(tictactoe_game())