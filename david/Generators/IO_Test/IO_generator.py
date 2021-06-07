import json
import random

def generateNumbers():

  random.seed(500)

  first_numbers = [random.randint(-50000, 50000) for _ in range (50)]  
  
  return first_numbers

def generateCase(case, first_number):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s" % (first_number)

  result = first_number
  new_case["output"] = "%s" % (result)

  return new_case

def generateTestCases():

  numbers = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(len(numbers)):
    tests.append(generateCase(i + 1, numbers[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('iostream.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

