import json
import random

def generateNumbers():

  random.seed(500)

# generator takes two numbers

  first_numbers = [random.randint(0, 101) for _ in range (50)]
  second_numbers = [random.randint(0, first_numbers + 1) for _ in range (50)]
  
  return first_numbers, second_numbers #a list with 50 values for each of these two will be returned

def generateCase(case, first_number, second_number):

#This is the outer bracket that we see in the json file for each case

  new_case = {} # a dictionary used for json file later

  new_case["case"] = case #we will have a for loop iterating dfor e.g. 50 times later

  # my code
  # r = int(input()) #getting an int for r

  # n = int(input()) #getting an int for n

  lst = [] #creating an empty list

  new_case["input"] = "%d %d" % (first_number, second_number) #adding elements to this value string

  #iterating till the range
  for i in range (n):
    ele = int(input())

    lst.append(ele) #adding the element

    new_case["input"] = new_case["input"] + " " + str(ele)

  from random import choice

  if (first_number == second_number):
    result = "too late"

  elif (first_number > second_number):
    result = choice([i for i in range(1 , first_number+1) if i not in lst])

    new_case["output"] =  result

  return new_case # "new_case" is a dictionary including case number, input and output as keys 

def generateTestCases():

  first_numbers, second_numbers = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(len(first_numbers)):
    tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i])) 
    #a list named "tests" containing 50 (len(first_numbers)) case, first number and second number
  
  test_cases["tests"] = tests # final dic with one key and a list as its value for the key which will be passed to the json file

  return test_cases

test_cases = generateTestCases()
with open('addition.json', 'w') as json_file: 
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)
