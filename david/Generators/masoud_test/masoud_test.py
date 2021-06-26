import json
import random

def generateNumbers():

    random.seed(500)
    first_numbers = []
    second_numbers = []
    
#for each of 50 samples, I will append room numbers ("second_nubers" times) to a list. 
#Therefor it will be a liust of 50 lists with different dimensions (1-100)
    lst_occupied = []
    
    
# for each of 50 samples, generator takes two numbers and a list of numbers
    for i in range(50):
        first_numbers.append(random.randint(0, 101)) #first number
        second_numbers.append(random.randint(0, first_numbers[i]+1)) #second number       
       
        lst_occupied.append([random.randint(0,first_numbers[i]) + 1 for _ in range(second_numbers[i])])

#             new_case["input"] = new_case["input"] + " " + str(ele)
                              
    return first_numbers,second_numbers,lst_occupied # list of 50 num # list of 50 num # list of 50 lists with different lengths

def generateCase(case, first_number, second_number, lst_occupied):

    new_case = {} # a dictionary used for json file later

    new_case["case"] = case #we will have a for loop iterating dfor e.g. 50 times later

  # my code
    # str_occupied = ' '.join(lst_occupied)
    
    # new_case["input"] = "%d %d" % (first_number, second_number) + str_occupied #adding elements to this value string

    # from random import choice

    # if (first_number == second_number):
    #     result = "too late"

    # elif (first_number > second_number):
    #     result = choice([i for i in range(1 , first_number+1) if i not in lst_occupied])

    # new_case["output"] =  result

    return new_case # "new_case" is a dictionary including case number, input and output as keys

def generateTestCases():

  first_numbers, second_numbers, first_occupied = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(50):
    tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i]), lst_occupied[i]) 
    tests.append(generateCase(i+1, first_numbers[i], second_numbers[i], first_occupied[i]))
    #a list named "tests" containing 50 (len(first_numbers)) case, first number and second number
  
  test_cases["tests"] = tests # final dic with one key and a list as its value for the key which will be passed to the json file

  return test_cases

test_cases = generateTestCases()
with open('addition.json', 'w') as json_file: 
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)