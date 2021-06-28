import json
import random
import math

# Kattis Question link: https://open.kattis.com/problems/conquestcampaign
# Solution translated from https://github.com/mpfeifer1/Kattis/blob/master/conquestcampaign.cpp

def generateNumRowsColsCells(count : int) -> (int,int,int):
    random.seed(count)

    numRows = random.randint(1,100)
    numCols = random.randint(1,100)
    numWeakCells = random.randint(1, 10000)

    return numRows, numCols, numWeakCells

def generateCell(count : int, numRows : int, numCols : int) -> (int,int):

    random.seed(count)
    x : int = random.randint(1,numRows)
    y : int = random.randint(1,numCols)

    return x,y

class CaseData:

    def __init__(self, numRows, numCols, numWeakCells, cellList : list[(int,int)]):
        self.numRows = numRows
        self.numCols = numCols
        self.numWeakCells = numWeakCells
        self.cellList = cellList


def generateInput(count : int) -> CaseData:

    numRows, numCols, numWeakCells = generateNumRowsColsCells(count)

    cellsList : list[(int,int)] = [generateCell(count + i, numRows,numCols) for i in range(numWeakCells)]

    return CaseData(numRows,numCols, numWeakCells, cellsList)   


def inRange(x : int, y : int, mx : int, my : int)->bool:
    return x >= 0 and y >= 0 and x < mx and y < my

def solve(caseData : CaseData) -> int:

    dx : list[int] = [-1, 1, 0, 0]
    dy : list[int] = [0, 0, 1, -1]
    inf : int = 1 << 29
    
    v : list[list[int]] = []
    for i in range(caseData.numRows):
        v.append([inf for _ in range(caseData.numCols)])

    queue : list[(int,int)] = []

    for x,y in caseData.cellList:
        queue.append((x-1,y-1))
        v[x-1][y-1] = 1
    
    hi : int = 1

    while len(queue) != 0:
        x,y = queue.pop(0)
        for i in range(4):
            nextX : int = x + dx[i]
            nextY : int = y + dy[i]

            if not inRange(nextX, nextY, caseData.numRows, caseData.numCols):
                continue
            
            if v[nextX][nextY] == inf:
                v[nextX][nextY] = v[x][y] + 1
                hi = v[nextX][nextY]
                queue.append((nextX,nextY))

    return hi 

def generateCase(case, input : CaseData ):

    new_case = {}  

    new_case["case"] = case
    inputStr = "%s %s %s\n" % (input.numRows, input.numCols, input.numWeakCells) 
    inputStr += "".join([str(x) + " " + str(y) + "\n" for x,y in input.cellList])

    #print(inputStr)
    new_case["input"] = inputStr
    #solution = solve(board,direction)     
   
    new_case["output"] = str(solve(input))

    return new_case

def generateTestCases():    

    test_cases = {}
    tests = []
    tests.append(generateCase(1,CaseData(3,4,3,[(2,2),(2,2),(3,4)])))
    for i in range(1,50):
        tests.append(generateCase(i + 1, generateInput(i)))
     
    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('ConquestCampaign.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)
