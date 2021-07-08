import json
import random
import math

# Kattis Question link: https://open.kattis.com/problems/queens
# Solution translated from https://github.com/mpfeifer1/Kattis/blob/master/queens.cpp
NUMQUEENS = 50
usedNumQueens = [-1] * NUMQUEENS

def generateNumQueens(count : int):
    random.seed(count)

    nq = random.randint(0,NUMQUEENS-1)


    if(usedNumQueens[nq] == -1):
        usedNumQueens[nq] = 1
    else:
        nq = -1
        for i in range(len(usedNumQueens)):
            if usedNumQueens[i] == -1:
                nq = i
    if nq == -1:       
        
        print("out of room")
    return nq

# Python program to solve N Queen 
# Problem using backtracking
  
# global N
# N = 4
  
# def printSolution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j])
#         print
  
  
# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(N, board, row, col):
  
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True
  
def solveNQUtil(N, board, col):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True
  
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
  
        if isSafe(N, board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
  
            # recur to place rest of the queens
            if solveNQUtil(N, board, col + 1) == True:
                return True
  
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
  
    # if the queen can not be placed in any row in
    # this colum col  then return false
    return False
  
# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one  of the
# feasible solutions.
def solveNQ(numQueens : int):
 
    board = []

    for i in range(numQueens):
        board.append([0 for _ in range(numQueens)])   
  
    if solveNQUtil(numQueens, board, 0) == False:
        #print ("Solution does not exist")
        return False, board
  
    #printSolution(board)
    return True, board



# def generateBoard(count : int):
    
#     numQueens = generateNumQueens(count)

#     correct, board = solveNQ(numQueens)

#     return correct, board

# class Board:

#     def __init__(self, board : list[list[int]]):
#         self.board = board

def generateCorrectInput():
    print("starting generate correct")
    correctBoards = []
    i = 0
    while len(correctBoards) < 25:
        numQueens = generateNumQueens(i)
        print("board size ", numQueens , " x ", numQueens)
        correct, board = solveNQ(numQueens)
        print("made a board")
        if correct:
            print("valid board")
            correctBoards.append(board)
        i += 1

    allQueenPositions = []
    print("fiunished making all complete boards")
    for i in range(len(correctBoards)):
        queenPositions : list[(int,int)] = []

        currentBoard : list[list[int]] = correctBoards[i]

        for row in range(len(currentBoard)):
            for col in range(len(currentBoard[row])):
                if(currentBoard[row][col] == 1):
                    queenPositions.append((row,col))
        allQueenPositions.append(queenPositions)


    return allQueenPositions


def generateDefaultInput(count : int) -> (list[list[(int,int)]]):    

    numQueens = generateNumQueens(count)

    queenPositions : list[(int,int)] = [(random.randint(0,numQueens-1),random.randint(0,numQueens-1)) for _ in range(numQueens)]
    
    return queenPositions


def generateInCorrectInput(count : int) -> (list[list[(int,int)]]):    

    numQueens = generateNumQueens(count)


    queenPositions : list[(int,int)] = [(random.randint(0,numQueens-1),random.randint(0,numQueens-1)) for _ in range(numQueens)]

    while solve(queenPositions) == "CORRECT":
        print("running")
        queenPositions = [(random.randint(0,numQueens-1),random.randint(0,numQueens-1)) for _ in range(numQueens)]

    return queenPositions

def generateCorrectInputEasy(count : int) -> (list[list[(int,int)]]):    

    numQueens = generateNumQueens(count)

    i = 0
    queenPositions : list[(int,int)] = [(random.randint(0,numQueens-1),random.randint(0,numQueens-1)) for _ in range(numQueens)]

    while solve(queenPositions) == "INCORRECT":
        print("running ",i)
        queenPositions = [(random.randint(0,numQueens-1),random.randint(0,numQueens-1)) for _ in range(numQueens)]
        i+=1

    return queenPositions



def solve(queenPositions : list[(int,int)]) -> str:

    size : int = len(queenPositions)

    diagonal : int = size * 2 - 1

    a : list[bool] = [False] * diagonal
    b : list[bool] = [False] * diagonal
    c : list[bool] = [False] * size
    d : list[bool] = [False] * size

    for x ,y in queenPositions:
        if a[y - x + size - 1] or b[x + y] or c[x] or d[y]:
            return "INCORRECT"
        a[y - x + size - 1] = True
        b[x + y] = True
        c[x] = True
        d[y] = True
    
    return "CORRECT"

def generateCase(case, input : list[(int,int)] ):

    new_case = {}  
    
    new_case["case"] = case
    inputStr = "%s\n" % (str(len(input))) 

    inputStr += "".join([str(x) + " " + str(y) + "\n" for x,y in input ])    
   
    new_case["input"] = inputStr  
   
    new_case["output"] = solve(input)

    return new_case

def generateTestCases():    

    test_cases = {}
    tests = []
    
    #correctQueenPositions = generateCorrectInput()

    # for i in range(25):
    #     tests.append(generateCase(i+1, correctQueenPositions[i]))        
    
    # for i in range(25,50):
    #     tests.append(generateCase(i + 1, generateInCorrectInput(i)))

    for i in range(50):
        tests.append(generateCase(i+1, generateDefaultInput(i)))

    for i in range(1):
        tests[i] = generateCase(i+1, generateCorrectInputEasy(i))
     
    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('Queens.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)


#correctQueenPositions = generateCorrectInput()

# for positions in allQueenPositions:
#     print(solve(positions))