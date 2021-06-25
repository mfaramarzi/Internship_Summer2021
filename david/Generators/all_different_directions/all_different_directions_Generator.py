import json
import random
import math

#solution translated from https://github.com/mpfeifer1/Kattis/blob/master/2048.cpp

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2))

class Vector2f:
    def __self__(x1 : float, y1: float):
        x = x1
        y = y1

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
with open('AllDifferentDirections.json', 'w') as json_file:
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