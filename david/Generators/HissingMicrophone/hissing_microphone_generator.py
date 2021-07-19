import json
import random

def generateRandomChar() -> str:
  random.seed()
  
  choice : str = chr(random.randint(97,122))
  return str(choice)

def generateHiss():
  random.seed() 
  strLen : int = random.randint(2,28)
  testStr = ""

  insertIndex = random.randint(1,strLen)

  for i in range(strLen):    
    testStr += generateRandomChar() 
  
  testStr = "ss" + testStr
  
  return testStr

# Generate random numbers as input
def generateString() -> str: 

  random.seed()
  strLen : int = random.randint(1,30)
  testStr = ""

  for i in range(strLen):    
    testStr += generateRandomChar() 
  
  return testStr

def solve(inStr) -> str:
  num = 0
  for char in inStr:
    if char == 's':
      num += 1
      if(num == 2):
        return "hiss"
    else:
      num = 0

  return "no hiss"



# Generate each individual test case
def generateCase(case, inStr):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s" % (inStr)

  result = solve(inStr)
  new_case["output"] = "%s" % (result)

  return new_case

# Create list of all 50 test cases with case #, input, expected output
def generateTestCases():

  numHissCases = 23
  numNoHissCases = 24
  test_cases = {}
  tests = []
  
  for i in range(3,50):
    if( i%2):
      tests.append(generateCase(i + 1, generateHiss()))
    else:
      tests.append(generateCase(i + 1, generateString())) 
  

  tests.insert(0, generateCase(1, "amiss"))
  tests.insert(1, generateCase(2, "octopuses"))
  tests.insert(2, generateCase(3, "hiss"))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('HissingMicrophone.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

