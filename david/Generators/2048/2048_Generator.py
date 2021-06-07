import json
import random
import math

#solution translated from https://github.com/mpfeifer1/Kattis/blob/master/2048.cpp

def generateBoard(count):

    choices = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    random.seed(count)
    board = []

    for i in range(4):
        board.append([choices[random.randint(0,10)] for _ in range(4)])
    return board

def generateDirection(count):
    random.seed(count)
    return random.randint(0,3)

def generateInput(count):
    board = generateBoard(count)
    direction = generateDirection(count)

    return board, direction

def swipe(v : list[int]) -> list[int]:
    
    # get non-zero elements
    
    v2 = [i for i in v if i != 0]


    v2.append(0)

    # merge together, left is emrged, right is 0
    for i in range(len(v2)-1):
        if v2[i] == v2[i+1]:
            v2[i] *= 2
            v2[i+1] = 0
    
    # slide left
    v3 : list[int] = []

    for i in range(len(v2)):
        if v2[i] != 0:
            v3.append(v2[i])
    # fille with zeroes
    blanks : int = 4 - len(v3)
    for i in range(blanks):
        v3.append(0)

    return v3


def solve(board, dir : int):    
    
    if dir == 0:       
        board = [swipe(board[i]) for i in range(len(board))]
    
    if dir == 1:
        for i in range(4):            
            v : list[int]= [board[x][i] for x in range(4)]
            v = swipe(v)

            for x in range(4):
                board[x][i] = v[x]
    
    if dir == 2:
        for i in range(4):            
            board[i].reverse()
            board[i] = swipe(board[i])
            board[i].reverse()
    
    if dir == 3:
        for i in range(4): 
            v : list[int] = [0] * 4
            for x in range(4):
                v[3-x] = board[x][i]

            v = swipe(v)

            for x in range(4):
                board[x][i] = v[3-x]
    return board        

def generateCase(case, input):

    new_case = {}

    board = input[0]
    direction = input[1]
    boardStr = ""  

    for row in board:      
        boardStr += "".join([str(ele) + ' ' for ele in row])
        boardStr = boardStr.strip()
        boardStr += "\n" 
    inputStr = boardStr + str(direction)

    new_case["case"] = case
    new_case["input"] = "%s" % (inputStr) 

    solution = solve(board,direction)  

    solStr = ""
    for row in solution:
        solStr+="".join([str(ele) + ' ' for ele in row])
        solStr = solStr.strip()
        solStr += "\n" 

   
    new_case["output"] = solStr

    return new_case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(generateInput(i))      
    testDir = 0
    testBoard = [[2,0,0,2],
             [4,16,8,2],
             [2,64,32,4],
             [1024,1024,64,0]]

    myTestCases[0] = (testBoard,testDir)

    test_cases = {}
    tests = []
    for i in range(50):
        tests.append(generateCase(i + 1, myTestCases[i]))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('2048.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

# testBoard = [[128,512,32,16],
#              [4,4,1024,0],
#              [32,256,128,512],
#              [2,32,256,512]]
# testDir = 3
# print(solve(testBoard,testDir))
# testBoard = [[128,512,32,16],
#              [4,4,1024,0],
#              [32,256,128,512],
#              [2,32,256,512]]
# testDir = 3
# sol = (solve(testBoard,testDir))
# print("----------------")
# print(sol)