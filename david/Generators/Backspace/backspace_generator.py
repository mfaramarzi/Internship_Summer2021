import json
import random

# https://open.kattis.com/problems/backspace

# < 60
# a - z 97 - 122

def solve(inString : str) -> str:
  outStr = ""
  
  for ch in inString:
    if ch == "<":
      outStr = outStr[:-1]
    else:
       outStr += ch

  return outStr


def generateStrings() -> list[str]:
  random.seed(45)
  stringList = []
  choices = [chr(i) for i in range(97,123)]

  
  for i in range(10):
    choices.append("<")

  for i in range(48):
    tempStr = ""
    strLength = random.randint(0,1000000)
    for j in range(strLength):
      tempStr += choices[random.randint(0,len(choices)-1)]
    stringList.append(tempStr)

  stringList.insert(0,"a<bc<")
  stringList.insert(1,"foss<<rritun")

  return stringList


# Generate each individual test case
def generateCase(case, inString):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s" % (inString)

  result = solve(inString)
  
  new_case["output"] = "%s" % (result)

  return new_case


def generateTestCases():

  stringList = generateStrings()

  test_cases = {}
  tests = []
  for i in range(len(stringList)):
    tests.append(generateCase(i + 1, stringList[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('Backspace.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

