import json
import random



def generateNumbers(): # function to return input data

    q_l_period = [[]]
    num_periods = []

    random.seed(500)

    for i in range (50):

        num_periods.append(random.randint(0, 101))  #Assigning a random number between 1 and 100

        for j in range (num_periods[i]):
            q_l_period.append([random.random() , random.randint(0, 101)]) # a list with 50 sublists each containing two elements

  
    return num_periods, q_l_period 
  # num_periods is a list of 50 numbers and q_l_period is a 2-d list of pair numbers including quality and num of years for each period





def generateCase(case, num_periods, q_l_period): #function including main code

    new_case = {}

    sum_q_l_period = 0 # QALY accumulated by the person

    str_q_l_period = ' '.join([str(i) for x in q_l_period for i in x]) #joining elements of a list made by list comprehension

    new_case["case"] = case

    new_case["input"] = str(num_periods) + " " + str_q_l_period #adding elements to this value string

    for i in range (50):

        sum_q_l_period += float(q_l_period[i][0]) * float (q_l_period[i][1])

    new_case["output"] = str(sum_q_l_period)

    return new_case



def generateTestCases():

    num_periods, q_l_period = generateNumbers()

    test_cases = {}
    tests = []

    # print(len(num_periods))
    # print(q_l_period)
    # print(num_periods)

    for i in range(len(num_periods)): #starts from 0 to 49
        tests.append(generateCase(i + 1, num_periods[i], q_l_period[i]))

    test_cases["tests"] = tests

    return test_cases





test_cases = generateTestCases()
with open('QALY.json', 'w') as json_file:
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)