#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random
import names


# In[2]:


def generateNumbers():#generating input numbers

    random.seed(500)

    name = [names.get_first_name() for _ in range (50)]

    return name


# In[3]:


def generateCase(case, name):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%s" %(name)
    
#     main code
    
    i = 0
    while (len(name) - 1 > i):

            if (name[i] == name[i+1]):

                name = name.replace(name[i], "" , 1)
                i-=1

            i+=1
    
    new_case["output"] = "%s" % (name)

    return new_case


# In[4]:


def generateTestCases(): #generating 50 test cases

    name = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(name)):
        
        tests.append(generateCase(i + 1, name[i]))

    test_cases["tests"] = tests

    return test_cases


# In[5]:


test_cases = generateTestCases() 


# In[6]:


with open('Apaxiaaaaaaaaaaaans.json', 'w') as json_file:
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




