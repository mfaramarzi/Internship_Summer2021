import json
import random

def generateNumbers():

    random.seed(500)
    num_judgs = []
    num_judge_rateds = []
    ratings = []
    
    # for each of 50 samples, generator takes two numbers and a list of numbers

    for i in range(50):
        num_judgs.append(random.randint(1, 10)) #first number
        num_judge_rateds.append(random.randint(0, num_judgs[i])) #second number
        ratings.append([random.randint(-3, 3) for _ in range(num_judge_rateds[i]) ]) #list comprehesion 
  
    # print(ratings)

    return num_judgs, num_judge_rateds , ratings #"ratings" is a 2d list

def generateCase(case, num_judg, num_judge_rated, ratings):

    new_case = {}

    str_ratings = ' '.join([str(x) for x in ratings]) #it will be executed for each of 50 samples, therefore a 1-d array 

    new_case["case"] = case
    new_case["input"] = "%s %s" % (num_judg, num_judge_rated) + " " +  str_ratings #here first and second number are strings!



    #my code

    sum_announced = 0

    min_sum_unannounced = 0

    max_sum_unannounced = 0

    for i in range(num_judge_rated): #sum of ratings of already announced rates
        
        sum_announced += sum(ratings)
        
    # calculating the minimum and maximum sum of unannounced rates

    for i in range (num_judg - num_judge_rated):
        
        min_sum_unannounced -= 3
        
        max_sum_unannounced += 3
        
    max_rate = (sum_announced + max_sum_unannounced) / num_judg

    min_rate = (sum_announced + min_sum_unannounced) / num_judg


    new_case["output"] = str(min_rate) + " " + str(max_rate)

    return new_case

def generateTestCases():

    num_judgs, num_judge_rateds , ratings= generateNumbers()

    test_cases = {}
    tests = []
    for i in range(len(num_judgs)):
        tests.append(generateCase(i + 1, num_judgs[i], num_judge_rateds[i] , ratings[i]))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('rating_problems.json', 'w') as json_file:
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)




