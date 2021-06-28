#!/usr/bin/env python
# coding: utf-8

# # Input
# 
# The input will contain 10 non-negative integers, each smaller than 1000
# , one per line.

# # Output
# 
# Output the number of distinct values when considered modulo 42
# on a single line.

# In[1]:


import json
import random

def generateNumbers():#generating input numbers

    random.seed(500)
    
    numbers_lst = []
    
    for i in range(50):
        
        numbers_lst.append([random.randint(0, 1000) for _ in range (10)]) 
    

    return numbers_lst


# In[11]:


def generateCase(case, numbers_lst):# generating a dic containing case, input, and result strings 
    
    counter = 0
    
    remainder_lst = []

    new_case = {}

    new_case["case"] = case

    new_case["input"] = " ".join([str(i) for i in numbers_lst])

    for i in range(len(numbers_lst)):
        
        remainder = numbers_lst[i] % 42
        
        if (remainder not in remainder_lst):
            
            remainder_lst.append(remainder)
            
            counter += 1
            
    new_case["output"] = counter

    return new_case


# In[12]:


def generateTestCases(): #generating 50 test cases

    numbers_lst = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(numbers_lst)):
        
        tests.append(generateCase(i + 1, numbers_lst[i]))

    test_cases["tests"] = tests

    return test_cases


# In[13]:


test_cases = generateTestCases() 

with open('Modulo.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




