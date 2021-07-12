import json
import random
import math


def generateNumRowsCols() -> (int,int):
    random.seed()
    return random.randint(1,100), random.randint(1,100)

def generateNumTestsPerCase() -> int:
    random.seed()

    return random.randint(1,50)

def generatestr() -> str:
    choices = ["#","-"]

    return choices[random.randint(0,1)]

def generateSky() -> list[list[str]]:
    random.seed()
    board = []
    numRows, numCols = generateNumRowsCols()

    for i in range(numRows):
        board.append([generatestr() for _ in range(numCols)])

    return board

def generateFullCase() -> list[list[list[str]]]:
    cases = []  
    random.seed()

    for i in range(generateNumTestsPerCase()):
        cases.append(generateSky())

    return cases

class Pixel:
    def __init__(self, c : str, used : bool):
        self.c = c
        self.used = used

    def copy(self, other : "Pixel"):
        self.c = other.c
        self.used = other.used

def floodFill(m : int, n: int, i: int, j: int, v : list[list[Pixel]]) -> int:
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    
   
   # p : Pixel = Pixel.copy(v[i][j])
    if v[i][j].used:
        return 0

    v[i][j].used = True

    floodFill(m, n, i, j + 1, v)
    floodFill(m, n, i, j - 1, v)
    floodFill(m, n, i + 1, j, v)
    floodFill(m, n, i - 1, j, v)

    return 1


def countingStars(sky : list[list[str]]) -> int:

    v : list[list[Pixel]] = []

    m = len(sky)
    n = len(sky[0])

    for i in range(len(sky)):
        temp : list[Pixel] = []
        for j in range(len(sky[i])):
            p : Pixel = Pixel(sky[i][j], sky[i][j] == '#')
            temp.append(p)
        v.append(temp)

    stars : int = 0

    for i in range(m):
        for j in range(n):
            stars += floodFill(m, n, i, j, v)

    return stars

        



def solve(cases) -> str:
    outStr = ""
    count : int = 1
    for case in cases:        
        tempStr = ""
        tempStr = ("Case " + str(count) + ": " + str(countingStars(case)) + "\n")
        outStr += tempStr
        count += 1

    return outStr

def generateCase(case, inputCase):

  new_case = {}
  inStr = ""
  
  for n in inputCase:
      inStr += str(len(n)) + " " + str(len(n[0])) + "\n"
      for row in n:          
          inStr += "".join(row) + "\n"

  new_case["case"] = case
  new_case["input"] = "%s" % (inStr) 

  solution = solve(inputCase)
  
  strSol = ""
  new_case["output"] = solution

  return new_case

def generateTestCases():

    myTestCases = []
    for i in range(49):        
        myTestCases.append(generateFullCase())
  
    board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-"],
    ["#", "#", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-"],
    ["#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "#"]]

    board1 = [
        ["#", "-", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["#", "-", "#", "#", "#", "#", "#", "#", "#", "#"]]

    case = []
    case.append(board)
    case.append(board1)

    myTestCases.insert(0,case)
    

    test_cases = {}
    tests = []
    for i in range(50):
        tests.append(generateCase(i + 1, myTestCases[i]))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('CountingStars.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

board2 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-"],
    ["#", "#", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-"],
    ["#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "-", "-"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "-", "#"]]

board3 = [
    ["#", "-", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["#", "-", "#", "#", "#", "#", "#", "#", "#", "#"]]


case = []
case.append(board2)
case.append(board3)

print(solve(case))

