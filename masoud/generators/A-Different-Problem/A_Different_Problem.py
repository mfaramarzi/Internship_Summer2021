#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random


# In[2]:


def generateNumbers():#generating input numbers

    random.seed(500)

    first_numbers = [random.randint(0, 1000000000000000) for _ in range (50)]
    
    second_numbers = [random.randint(0, 1000000000000000) for _ in range (50)]

    return first_numbers, second_numbers


# In[3]:


def generateCase(case, first_number, second_number):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%s %s" % (first_number, second_number)

    result = first_number - second_number
    
    if (result < 0):
        
        result = -result
    
    new_case["output"] = str(result)

    return new_case


# In[4]:


def generateTestCases(): #generating 50 test cases

    first_numbers, second_numbers = generateNumbers()

    test_cases = {}
    tests = []
    for i in range(len(first_numbers)):
        
        tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i]))

    test_cases["tests"] = tests

    return test_cases


# In[5]:


test_cases = generateTestCases() 


# In[6]:


with open('A_Different_Problem.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




