#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random

def generateNumbers():#generating input numbers

    random.seed(500)

    sum_num = [random.randint(0 , 1000) for _ in range (50)]
    diff_num = [random.randint(0 , 1000) for _ in range (50)]

    return sum_num, diff_num


# In[3]:


def generateCase(case, sum_num, diff_num):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case

    new_case["input"] = "%d %d" % (sum_num, diff_num)

    a = (sum_num + diff_num)/2
    
    b = a - diff_num
    
    if (( a * 2 == sum_num + diff_num ) and ( b >= 0 )):
    
        new_case["output"] = " %s %s " %(a, b)
        
    else:
        new_case["output"] = "impossible"

    return new_case


# In[4]:


def generateTestCases(): #generating 50 test cases

    sum_num, diff_num = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(sum_num)):
        
        tests.append(generateCase(i + 1, sum_num[i], diff_num[i]))

    test_cases["tests"] = tests

    return test_cases


# In[5]:


test_cases = generateTestCases() 

with open('Beat_the_Spread.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




