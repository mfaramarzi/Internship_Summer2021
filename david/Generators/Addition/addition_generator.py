import json
import random

# Generate random numbers as input
def generateNumbers() -> (list[int], list[int]): 

  random.seed(500)

  first_numbers = [random.randint(-50000, 50000) for _ in range (50)]
  second_numbers = [random.randint(-50000, 50000) for _ in range (50)]
  
  return first_numbers, second_numbers

# Generate each individual test case
def generateCase(case, first_number, second_number):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s %s" % (first_number, second_number)

  result = first_number + second_number
  new_case["output"] = "%s + %s = %s" % (first_number, second_number, result)

  return new_case

# Create list of all 50 test cases with case #, input, expected output
def generateTestCases():

  first_numbers, second_numbers = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(len(first_numbers)):
    tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('addition.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

