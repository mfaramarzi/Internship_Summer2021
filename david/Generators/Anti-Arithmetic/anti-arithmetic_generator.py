import json
import random
import math

def antiArithmetic(n, v, pos):
    for i in range(len(v)):
        pos[v[i]] = i

    for s in range(n):
        for d in range(-n,n+1):
            if (s+d+d >= 0 and s + d + d < n):
                if (pos[s] < pos[s+d] and pos[s+d] < pos[s+d+d]):
                   
                    return "no"

    
    return "yes"

def solve(input : str):
    cases = []
    save = 0

    solution = []

    for i in range(len(input)):
        if input[i] == "\n":
            cases.append(input[save:i])
            save = i+1

    caseList = [case.split() for case in cases]  
   
    numbers = []
    for case in caseList:
        numbers.append(int(case[0].strip(':')) )
        case.pop(0)

    for i in range(len(caseList)):
        num = numbers[i]
        vList = [int(case) for case in caseList[i]]
        posList = [-1] * num

        solution.append(antiArithmetic(num,vList,posList))
    solStr = "".join([str(sol) + "\n" for sol in solution])
    
    solStr = solStr[:-1:]
    

    return solStr
        

    

def generateProgressions():

    random.seed()

    numCases = random.randint(1,5)
    cases = ""

    for i in range(numCases):
        randNum = random.randint(3,100)
        currentCase = [n for n in range(0,randNum)]
        random.shuffle(currentCase)    
    
        caseStr = str(randNum) + ": " + ' '.join([str(num) + " " for num in currentCase])
        cases += (caseStr) + "\n"
    cases += "0"
    
    return cases

def generateCase(case, input):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s" % (input) 

  solution = solve(input)
 
  new_case["output"] = solution
  
  print(new_case)

  return new_case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(generateProgressions())   
    myTestCases[0] =  "3: 0 2 1 \n5: 2 0 1 3 4 \n6: 2 4 3 5 0 1 \n0"
    
    test_cases = {}
    tests = []
    for i in range(len(myTestCases)):
        tests.append(generateCase(i + 1, str(myTestCases[i])))
    
    
    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('Anti-Arithmetic.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

