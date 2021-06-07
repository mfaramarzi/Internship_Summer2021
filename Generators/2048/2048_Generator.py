import json
import random
import math

def solution():
    

def solve(input : str):
    cases = []
    inputList = input.split()
   
    totalCases = int(inputList.pop(0))
    currentStart = 0
    for i in range(totalCases):
        currentLength = int(inputList.pop(currentStart))
      
        currentCase = []       
        for j in range(currentStart, currentStart + currentLength):
            currentCase.append(inputList[j])
        cases.append(currentCase)
        currentStart = currentStart + currentLength

    return AboveAverage(cases)

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




def generateCase(case, input):

  new_case = {}

  board = input[0]
  direction = input[1]

  boardStr = ""

  boardStr.join(board)
  print(boardStr)

  new_case["case"] = case
  new_case["input"] = "%s" % (input.strip()) 

  solution = solve(input)
  
  strSol = " ".join(solution) 
  new_case["output"] = strSol.replace(" ","")

  return new_case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(generateInput(i))      

    test_cases = {}
    tests = []
    for i in range(50):
        tests.append(generateCase(i + 1, myTestCases[i]))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('AboveAverage.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

