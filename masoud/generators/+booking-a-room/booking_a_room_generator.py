
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

        first_numbers.append(random.randint(0, 100)) #first number #the second number is inclusive in random.randint(0, 100)

        second_numbers.append(random.randint(0, first_numbers[i])) #second number

        lst_occupied.append([random.randint(0,first_numbers[i]) for _ in range(second_numbers[i]) ]) ''' since in each iteration I am 
        appending a list to the "lst_occupied", it will be a 2d list  '''

    
    
    # print(lst_occupied)                          
    return first_numbers,second_numbers,lst_occupied # list of 50 num # list of 50 num # list of 50 lists with different lengths




def generateCase(case, first_number, second_number, lst_occupied):

    new_case = {} # a dictionary used for json file later

    new_case["case"] = case #we will have a for loop iterating dfor e.g. 50 times later

    str_occupied = ' '.join([str(x) for x in lst_occupied ])
    
    new_case["input"] = "%d %d" % (first_number, second_number) + " " + str_occupied #adding elements to this value string

    from random import choice

    result = " "

    if (first_number == second_number):

        result = "too late"

    elif (first_number > second_number):

        result = choice([i for i in range(1 , first_number+1) if i not in lst_occupied]) #Return a random element from the list of unoccupied rooms

    new_case["output"] =  result

    return new_case # "new_case" is a dictionary including case number, input and output as keys 



def generateTestCases():

    first_numbers, second_numbers, lst_occupied = generateNumbers()

    test_cases = {}
    tests = []
    for i in range(len(first_numbers)):
        tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i], lst_occupied[i])) 
        #a list named "tests" containing 50 (len(first_numbers)) case, first number and second number
  
    test_cases["tests"] = tests # final dic with one key and a lisReturn a random element from a list:t as its value for the key which will be passed to the json file

    return test_cases


test_cases = generateTestCases()
with open('addition.json', 'w') as json_file: 
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)

