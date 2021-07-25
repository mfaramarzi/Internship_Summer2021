#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json
import random


# In[3]:


def generateNumbers():#generating input numbers

    random.seed(500)

    hours = [random.randint(0, 23) for _ in range (50)]
    minutes = [random.randint(0, 59) for _ in range (50)]

    return hours, minutes


# In[15]:


def generateCase(case, hours, minutes):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case

    new_case["input"] = "%d %d" % (hours, minutes)

    if (hours == 0 and minutes < 45):
        
        hours = 23
        minutes = 60 + minutes - 45
        
    elif(hours == 0 and minutes >= 45):
        
        hours = hours
        
        minutes = minutes - 45
        
    elif(hours != 0 and minutes < 45):
        
        hours = hours -1
        
        minutes = 60 + minutes - 45
        
    elif(hours != 0 and minutes > 45):
        
        hours = hours
        
        minutes = minutes - 45
        
    new_case["output"] = "%d %d" % (hours , minutes)

    return new_case


# In[16]:


def generateTestCases(): #generating 50 test cases

    hours , minutes = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(hours)):
        
        tests.append(generateCase(i + 1, hours[i], minutes[i]))

    test_cases["tests"] = tests

    return test_cases


# In[17]:


test_cases = generateTestCases() 


# In[18]:


with open('Spavanac.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




