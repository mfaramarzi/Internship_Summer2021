#!/usr/bin/env python
# coding: utf-8

# # Input
# 
# The input consists of n
# cases, and the first line consists of one positive integer giving n. The next n lines each contain 3 integers, r, e and c. The first, r, is the expected revenue if you do not advertise, the second, e, is the expected revenue if you do advertise, and the third, c, is the cost of advertising. You can assume that the input will follow these restrictions: 1≤n≤100, −106≤r,e≤106 and 0≤c≤106.

# # Output
# 
# Output one line for each test case: “advertise”, “do not advertise” or “does not matter”, indicating whether it is most profitable to advertise or not, or whether it does not make any difference.

# In[1]:


import json
import random


# In[2]:


# A func to generate 50 input values and return them as seperate lists

def generateNumbers():

    random.seed(500)

    rev_no_adv = [random.randint(1, 100) for _ in range (50)]
    
    rev_adv = [random.randint(-106, 106) for _ in range (50)]
    
    cost_adv = [random.randint(0, 106) for _ in range (50)]

    return rev_no_adv, rev_adv, cost_adv


# In[12]:


# generating a dic containing case, input, and result strings 

def generateCase(case, rev_no_adv, rev_adv, cost_adv):

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%s %s %s" % (rev_no_adv, rev_adv, cost_adv)

    if (rev_adv - rev_no_adv > cost_adv):
        new_case["output"] = "advertise"
    
    elif (rev_adv - rev_no_adv == cost_adv):
        new_case["output"] = "does not matter"

    elif (rev_adv - rev_no_adv < cost_adv):
        new_case["output"] = "do not advertise"
    
    return new_case


# In[17]:


def generateTestCases(): #generating 50 test cases

    rev_no_adv, rev_adv, cost_adv = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(rev_no_adv)):
        
        tests.append(generateCase(i + 1, rev_no_adv[i], rev_adv[i], cost_adv[i]))

    test_cases["tests"] = tests

    return test_cases


# In[18]:


test_cases = generateTestCases() 

with open('Nasty_Hacks.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:





# In[ ]:




