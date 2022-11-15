# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import getprintBoard
from logic import getInput
from logic import moveChess
from logic import other_player
from logic import get_winner

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 1 #player1 denoted in "X", player2 denoted in "O"
    Turn=0
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print(getprintBoard(board))
        # TODO: Input a move from the player.
        instream = input("Player{} please choose a position in format x,y to place chess:".format(player))
        x,y=getInput(instream,board)
        # 判断输入是否符合规范 if (x, y) == (-1, -1):
            #print("Wrong input, please input coordinate in format x,y!")
            #continue
        # TODO: Update the board.
        board=moveChess(player,x,y,board)
        winner=get_winner(board)
        # TODO: Update who's turn it is.
        player=other_player(player)
        Turn+=1 # 相当于 Turn = Turn+1
        if Turn==9:
            break
    print(getprintBoard(board))
    if winner==None:
        print("Draw!")
    else:
        print("Player{} win the game!".format(winner)) #.表示后面的东西是前面的类成员，format是字符串类的一种成员函数
