import json
import random
import math

def AboveAverage(cases):
    output = []
    
    for case in cases:       
        total = 0
        for grade in case:
            total += int(grade)
       
        average = total / len(case) 
        
        better = 0
        for studentGrade in case:
            if int(studentGrade) > average:                
                better += 1
        
        perc = 100.0 * better/float(len(case))
        perc = "{:.3f}".format(perc)
        output.append(perc + "%\n")
    
    return output

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


def generateInnerCases(count : int):

    random.seed(count * 10)

    numCases = random.randint(1,50)
    cases = ""
    cases += str(numCases) + "\n"

    for i in range(numCases):
        numPeople = random.randint(1,1000)
        currentCase = [random.randint(0,100) for n in range(0,numPeople)]          
    
        caseStr = str(numPeople) + " " + ' '.join([str(num) + " " for num in currentCase])
        cases += (caseStr) + "\n"
    cases = cases[:-1:]

    return cases

def generateCase(case, input):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s" % (input.strip()) 

  solution = solve(input)
  
  strSol = " ".join(solution) 
  new_case["output"] = strSol.replace(" ","")

  return new_case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(generateInnerCases(i))      
    myTestCases[0] = "5\n5 50 50 70 80 100\n7 100 95 90 80 70 60 50\n3 70 90 80\n3 70 90 81\n9 100 99 98 97 96 95 94 93 91"

    test_cases = {}
    tests = []
    for i in range(50):
        tests.append(generateCase(i + 1, str(myTestCases[i])))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('AboveAverage.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

