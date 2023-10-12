"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    a=0
    b=0
    for row in range(3):
        for col in range(3):
            if board[row][col]==X:
                a+=1
            if board[row][col]==O:
                b+=1
    if a==b:
        return X
    else:
        return O



def actions(board):
    able_actions=set()
    for row in range(3):
        for col in range(3):
            if board[row][col]==EMPTY:
                able_actions.add((row,col))
    return able_actions



def result(board, action):
    if action not in actions(board):
        raise Exception("not a valid action")
    row, col = action
    board_copy=copy.deepcopy(board)
    board_copy[row][col]=player(board)
    return board_copy


def checkRow(board, player):
    for row in range(3):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            return True
    return False

def checkCol(board, player):
    for col in range(3):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            return True
    return False

def checkDiag(board, player):
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return True
    elif board[0][2]==player and board[1][1]==player and board[2][0]==player:
        return True
    else:
        return False

def winner(board):
    if checkRow(board,X) or checkCol(board,X) or checkDiag(board,X):
        return X
    elif checkRow(board,O) or checkCol(board,O) or checkDiag(board,O):
        return O
    else:
        return None



def terminal(board):
    if winner(board) != None:
        return True
    for x in range(3):
        for y  in range(3):
            if board[x][y]==EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board)== O:
        return -1
    else:
        return 0

def max_value(board):
    v=-math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=max(v, min_value(result(board,action)))
    return v

def min_value(board):
    v=math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v, max_value(result(board,action)))
    return v


def minimax(board):
    if terminal(board):
        return None
    elif player(board)==X:
        plays=[]
        for action in actions(board):
            #add in plays list a tupple with the min_value and the action that results to its value
            plays.append([min_value(result(board,action)),action])
        #reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board)==O:
        plays=[]
        for action in actions(board):
            plays.append((max_value(result(board,action)),action))
        return sorted(plays, key=lambda x: x[0])[0][1]