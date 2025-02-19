def display(board):
    print('   |    |  ')
    print(' ' + board[7]+ ' | ' + board[8]+ '  | ' + board[9])
    print('   |    |  ')
    print('-----------')
    print('   |    |  ')
    print(' ' + board[4]+ ' | ' + board[5]+ '  | ' + board[6])
    print('   |    |  ')
    print('-----------')
    print('   |    |  ')
    print(' ' + board[1]+ ' | ' + board[2]+ '  | ' + board[3])
    print('   |    |  ')
def user_input():
    
    choice= input("Enter your choice ('X','O')  ")
    if choice=='X'or choice =='x':
        player1='X'
        player2='O'
    else:
        player2='X'
        player1='O'
    print("Player1: ",player1)
    print("Player2: ",player2)
    return player1, player2  
def updates(board):
    pos= int(input("Enter your position(1-9): "))
    if pos in range(1,10) and board [pos] ==' ':
        mark= input("Enter your value(x,o): ")
        board[pos] = mark
        return board
    else:
        print("Invalid position!")  
def check(board,mark):
    if ((board[7] == mark and board[8] == mark and board[9] == mark) or 
       (board[4] == mark and board[5] == mark and board[6] == mark) or 
       (board[1] == mark and board[2] == mark and board[3] == mark) or 
       (board[7] == mark and board[4] == mark and board[1] == mark) or 
       (board[8] == mark and board[5] == mark and board[2] == mark) or 
       (board[9] == mark and board[6] == mark and board[3] == mark) or 
       (board[7] == mark and board[5] == mark and board[3] == mark) or 
       (board[9] == mark and board[5] == mark and board[1] == mark)):
       return True
    return False     
def replay():
    choice = input("Dou want to play again? (y/n): ")
    return choice == 'y'
game_on = True
game_list=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
while game_on :
    print("Welcome to the tic tac toe game !!")
    print("Here is the current board ->")
    display(game_list)
    choice= input("Are u ready to play (Y&N): ")
    if choice== 'Y' or choice =='y':
        player1, player2 = user_input()
        turn = 'player1'
        print("Now the turn is :",turn)
        while True:
            res=updates(game_list)
            display(res)
            if check(game_list, player1):
                print("Player 1 wins!")
                break
            elif check(game_list, player1):
                print("Player2 wins!")
                break
            turn = player1 if turn == player2 else player2
        game_on = replay()
    else:
        print("Ok ! Thank you for visiting.")
        game_on = False
        
                 