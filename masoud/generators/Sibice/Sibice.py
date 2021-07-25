#!/usr/bin/env python
# coding: utf-8

# In[23]:


import json
import random
import math


# In[24]:


def generateNumbers():#generating input numbers

    random.seed(500)

    num_matches_lst = [random.randint(1, 50) for _ in range (50)]
    
    box_width_lst = [random.randint(1, 100) for _ in range (50)]
    
    box_length_lst = [random.randint(1, 100) for _ in range (50)]
    
    #50 nested lists of "num_matches_lst" length of matches
    match_length_lst = [[random.randint(1, 1000) for i in range (num_matches_lst[j])] for j in range (50)]

    return num_matches_lst, box_width_lst, box_length_lst, match_length_lst


# In[25]:


generateNumbers()


# In[41]:


def generateCase(case, num_matches_lst, box_width_lst, box_length_lst, match_length_lst):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%d %d %d" %(num_matches_lst, box_width_lst, box_length_lst)
    
    for i in range(len(match_length_lst)):
        
        new_case["input"] = new_case["input"] + "\n" + str(match_length_lst[i])
        
    new_case["output"] = ""
    
    for i in range (num_matches_lst):

        largest_length = math.sqrt(box_width_lst**2 + box_length_lst**2)
    
        if (match_length_lst[i] <= largest_length):
        
            new_case["output"] = new_case["output"] + "\n" + "DA"
            
        else:
            
            new_case["output"] = new_case["output"] + "\n" + "NE"
            
        

    return new_case


# In[42]:


def generateTestCases(): #generating 50 test cases

    num_matches_lst, box_width_lst, box_length_lst, match_length_lst = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(num_matches_lst)):
        
        tests.append(generateCase(i + 1, num_matches_lst[i], box_width_lst[i], box_length_lst[i], match_length_lst[i]))

    test_cases["tests"] = tests

    return test_cases


# In[43]:


test_cases = generateTestCases() 


# In[44]:


with open('Sibice.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




