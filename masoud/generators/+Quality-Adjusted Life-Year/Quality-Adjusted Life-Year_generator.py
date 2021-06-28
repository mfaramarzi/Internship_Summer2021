import json
import random



def generateNumbers(): # function to return input data

    q_l_period = []
    
    num_periods = []

    random.seed(500)

    for i in range (50):

        each_q_l_period = []

        num_periods.append(random.randint(0, 100))  #Assigning a random number between 1 and 100 for num of periods

        for j in range (num_periods[i]):

            each_q_l_period.append([random.random() , random.randint(0, 100)]) # a list with "num_periods" sublists each containing two elements
        q_l_period.append(each_q_l_period) # a list with 50 sublists each with "num_periods" sublists each containing two elements

    # print(num_periods)
    # print(q_l_period)
    # type(q_l_period[0])
    return num_periods, q_l_period 
  # num_periods is a list of 50 numbers and q_l_period is a 3-d list of 50 sublists each with "num_periods" sublists each containing two elements

def generateCase(case, num_periods, q_l_period): #function including main code

    new_case = {}

    sum_q_l_period = 0 # QALY accumulated by the person

    str_q_l_period = ' '.join([str(x) for x in q_l_period]) #joining list elements of a nested list made by list comprehension

    new_case["case"] = case

    new_case["input"] = str(num_periods) + " " + str_q_l_period #making input string containing "num_periods" and periods' "quality" and "years" pair lists

    
    for i in range (num_periods):

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
        tests.append(generateCase(i + 1, num_periods[i], q_l_period[i]))#it retuen new case dictionaries and append them to a list ("tests")

    test_cases["tests"] = tests # "tests" is assigned to the test_cases dictionary

    return test_cases





test_cases = generateTestCases()
with open('QALY.json', 'w') as json_file:
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)