# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random


#Create an empty board

#def make_empty_board():
    #board=[[".",".","."],
        #[".",".","."],
        #[".",".","."]]
    #return board


class Game:
    def __init__(self, playerX, player0):
        self.board = [
            [None,None,None],
            [None,None,None],
            [None,None,None],
        ]
        self._playerX = playerX
        self._player0 = player0
        self.game_not_over = True
        self.current_player = playerX
    
    def run(self):
        while self.game_not_over:
            self.make_move(self.board,self.current_player)
    
    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        #0~2 record 1~3 rows, 3~5 record 1~3 columns, 6,7 record crosses
        self.sameChessSum = [0 for i in range(8)]
        for i in range(3):
            for j in range(3):
                if board[j][i] == "X":
                    self.sameChessSum[j] += 1
                elif board[j][i]=="O":
                    self.sameChessSum[j] -=1

                if board[i][j] == "X":
                    self.sameChessSum[j+3] += 1
                elif board[i][j]=="O":
                    self.sameChessSum[j+3] -=1
            if board[i][i] == "X":
                self.sameChessSum[6] += 1
            elif board[i][i]=="O":
                self.sameChessSum[6]-=1

            if board[i][2 - i] == "X":
                self.sameChessSum[7] += 1
            elif board[i][2-i]=="O":
                self.sameChessSum[7]-=1
        if 3 in self.sameChessSum:
            return "X"
        elif -3 in self.sameChessSum:
            return "O"
        else:
            return None

    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player==self._player0:
            return self._playerX
        elif player==self._playerX:
            return self._player0

    #transfer the game board format for output
    def getprintBoard(self,board): #变成字符输出
        outBoard="" #告诉python这个outboard要存储一个字符串
        for i in range(len(board)):
            outBoard+="".join([v if v is not None else "." for v in board[i]])+"\n" # “”.oin是把列表里所有的元素拼在一起
        return outBoard

    #format input
    def transferInput(self,instream): #把用户输入的字符串转换为系统能够识别的坐标
        try:
            x, y = map(int, instream.split(","))
        except:
            return -1,-1
        #Transfer input coordinate to list index
        return x, y

    #check transferred input
    def checkInput(self,x,y,board): #判断用户输入的坐标o不ok

        if not ((x in range(3)) and (y in range(3))):
            #print("Input a wrong coordinate, the input x,y both in range (1,3)!")
            return -1,-1
        elif board[x][y] is not None:
            #print("There already is a chess on that position!")
            return -1,-1
        else:
            return x,y
    #Get input in string format
    def getInput(self, instream,board):
        x, y = self.transferInput(instream)
        x, y = self.checkInput(x, y,board)
        return x,y

    #Perform a move on the board
    def moveChess(self, player,x,y,board):
        board[x][y]=player.name

    def make_move(self, board, current_player):
        # TODO: Show the board to the user.
        print(self.getprintBoard(board))
        # TODO: Input a move from the player.
        x, y = current_player.get_move(self)
        if x == -1:
            print("Please input a valid position!")
            return
        # TODO: Update the board.
        self.moveChess(current_player, x, y, board)
        # TODO: Update who's turn it is.
        winner = self.get_winner(board)
        if winner is None and any([v is None for row in self.board for v in row]):
            self.current_player = self.other_player(current_player)
        else:
            self.game_not_over = False
            if winner is not None:
                print("Player %s win!" % current_player.name)
            else:
                print("Draw!")
            print(self.getprintBoard(board))

    

class Human:
    def __init__(self, name):
        self.name = name

    def get_move(self,game):
        instream = input("Player{} please choose a position in format x,y to place chess:".format(self.name))
        x, y = game.getInput(instream, game.board)
        return x,y
    
    def __repr__(self):
        return str(self.name)

class Bot(Human):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self,game):
        available_positions = [
            (i, j)
            for i in range(len(game.board))
            for j in range(len(game.board[i]))
            if game.board[i][j] is None
        ]
        return random.choice(available_positions)


game = Game(Human('X'),Bot('O'))
game.run()

##########################################
# #Deprecated
# def switchPlayer(player):
#     if player==1:
#         player=2
#     elif player==2:
#         player=1
#     return player

# #Deprecated
# #check whether the player win the game
# def checkWinner(x,y,board):
#     playerChess=board[x][y]
#     sameChessSum=[0,0,0,0]
#     for i in range(3):
#         if board[x][i]==playerChess:
#             sameChessSum[0]+=1
#         if board[i][y]==playerChess:
#             sameChessSum[1]+=1
#         if board[i][i]==playerChess:
#             sameChessSum[2]+=1
#         if board[i][2-i]==playerChess:
#             sameChessSum[3]+=1
#     if 3 in sameChessSum:
#         return True
#     else:
#         return False

# player=1
# while True:
#     if player ==1:
#         instream=input("Player1 please choose a position in format x,y to place chess:")
#         x,y=transferInput(instream)
#         x,y=checkInput(x,y)
#         if (x,y)==(-1,-1):
#             continue
#         board[x][y]="X"
#         printBoard(board)
#         if checkWinner(x,y,board):
#             print("Player1 win the game!")
#             break
#         player=2
#
#     elif player==2:
#         instream=input("Player2 please choose a position in format x,y to place chess:")
#         x,y=transferInput(instream)
#         x,y=checkInput(x,y)
#         if (x,y)==(-1,-1):
#             continue
#         board[x][y] = "O"
#         printBoard(board)
#         if checkWinner(x,y,board):
#             print("Player2 win the game!")
#             break
#         player=1