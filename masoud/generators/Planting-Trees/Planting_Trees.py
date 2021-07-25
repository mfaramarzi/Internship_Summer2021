#!/usr/bin/env python
# coding: utf-8

# In[24]:


import json
import random


# In[25]:


def generateNumbers():#generating input numbers

    random.seed(500)

    num_seedlings = [random.randint(1, 100) for _ in range(50)]
    
#     a 2-d list
    growth_times = [[random.randint(1, 1000) for i in range(num_seedlings[j])]
                    
                    for j in range (50)]

    return num_seedlings, growth_times


# In[26]:


def generateCase(case, num_seedlings, growth_times):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = str(num_seedlings)
    
    new_case["input"] = new_case["input"] + "\n" + " ".join([str(i) for i in growth_times])
    
    sorted_growth_times = sorted(growth_times, reverse = True) #point is here. normally iot is in ascending order. I want it to be in descending order
    
#     print(sorted_growth_times)
    
    max_time = max(sorted_growth_times)

    result = max_time + 1
    
    for i in range (1 , num_seedlings):
        
        if (sorted_growth_times[i] > max_time - i):
            
            result += 1 
    
    new_case["output"] = str(result + 1)

    return new_case


# In[27]:


def generateTestCases(): #generating 50 test cases

    num_seedlings, growth_times = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(num_seedlings)):
        
        tests.append(generateCase(i + 1, num_seedlings[i], growth_times[i]))

    test_cases["tests"] = tests

    return test_cases


# In[31]:


# generateTestCases()


# In[29]:


test_cases = generateTestCases() 


# In[30]:


with open('Planting_Trees.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




