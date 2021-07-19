import json
import random



def solve(spaceJunkNumbers) -> int:
  low = spaceJunkNumbers[0]
  lowIdx = 0

  for i in range(len(spaceJunkNumbers)):
    if(spaceJunkNumbers[i] < low):
      low = spaceJunkNumbers[i]
      lowIdx = i
    
  return lowIdx

def generateNumbers() -> list[int]:
  random.seed()
  numDays = random.randint(1,100000)
  junkList = []

  for i in range(numDays):
    junkList.append(random.randint(0,1000000000))
  return junkList




# Generate each individual test case
def generateCase(case, spaceJunkNumbers : list[int]):

  new_case = {}
  numDays = len(spaceJunkNumbers)

  inStr = "".join([str(i) for i in spaceJunkNumbers])

  new_case["case"] = case
  new_case["input"] = "%s" % (inStr)

  result = solve(spaceJunkNumbers)
  new_case["output"] = "%s" % (result)

  return new_case

# Create list of all 50 test cases with case #, input, expected output
def generateTestCases():

  
  test_cases = {}
  tests = []
  
  for i in range(1,50):    
      tests.append(generateCase(i + 1, generateNumbers()))

  tests.insert(0, generateCase(1, [3,4,1,7,2]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('LicenseToLaunch.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

