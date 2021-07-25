#!/usr/bin/env python
# coding: utf-8

# In[44]:


import json
import random


# In[45]:


def generateNumbers():#generating input numbers

    random.seed(500)

    width = [random.randint(1, 10000) for _ in range (50)]
    
    num_pieces = [random.randint(1, 5000) for _ in range (50)]
    
    w_l_pieces = [[(random.randint(1, 10000),random.randint(1, 10000))

                      for i in range (num_pieces[j])] for j in range (50)]

    return width, num_pieces, w_l_pieces


# In[46]:


generateNumbers()


# In[47]:


def generateCase(case, width, num_pieces, w_l_pieces):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%d\n%d" % (width, num_pieces)
    
    for i in range (num_pieces):

        new_case["input"] = new_case["input"] + "\n" + "%d %d\n" %(w_l_pieces[i][0], w_l_pieces[i][1])
#     my code

    area = 0
    
#     for i in range (num_pieces):
        
#         area += int(w_l_pieces[i].split(" ")[0]) * int(w_l_pieces[i].split(" ")[1]) 


    for i in range (num_pieces):
        
        area += w_l_pieces[i][0] * w_l_pieces[i][1] 

    
    L = int((area/width))

    new_case["output"] = str(L)

    return new_case


# In[48]:


def generateTestCases(): #generating 50 test cases

    width, num_pieces, w_l_pieces = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(width)):
        
        tests.append(generateCase(i + 1, width[i], num_pieces[i] , w_l_pieces[i]))

    test_cases["tests"] = tests

    return test_cases


# In[49]:


test_cases = generateTestCases() 


# In[50]:


with open('Shattered_Cake.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:





# In[ ]:




