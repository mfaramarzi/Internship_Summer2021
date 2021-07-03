#!/usr/bin/env python
# coding: utf-8

# In[60]:


import json
import random


# In[61]:


def generateNumbers():#generating input numbers

    random.seed(500)

    course_lst = []

    num_stu = [random.randint(1, 10000) for _ in range (50)]
    
#     code below also could be written in a for loop
    for i in range(50):
        
        course_lst.append([[random.randint(100, 499) for k in range (5)] for j in range (num_stu[i])])
        
        
#     course_lst.append([[random.randint(100, 499) for k in range (5)] for j in range (num_stu[i])] for i in range (50)) #nested list comprehension
    
    return num_stu, course_lst


# In[62]:


def generateCase(case, num_stu, course_lst): # generating a dic containing case, input, and result strings 

#course_lst is 3-d list and will be 2-d for each of 50 cases

    comb_cours_lst = [] #list of unique combinations of course

    new_case = {}

    new_case["case"] = case

    new_case["input"] = str(num_stu) + " " + " ".join([str(i) for i in course_lst]) # "i" is list of int initially. 
    

    for i in course_lst:#for the only 3-d list in the 4-d list 
        
        if set(i) not in comb_cours_lst: #each i is a 1-d list which will be converted to a set
            
            comb_cours_lst.append(set(i)) # it will result a list of sets
            
    uniq_comb = len(comb_cours_lst)  
    
    new_case["output"] = str(uniq_comb) #converting result from int to str

    return new_case


# In[63]:


def generateTestCases(): #generating 50 test cases

    num_stu, course_lst = generateNumbers()
    
#     print(num_stu)
#     for i in range(50):
#         print(course_lst[i])#why is it 4-d?!!

    test_cases = {}
    
    tests = []
#     for i in range(len(num_stu)): #length of "num_stu" list
        
#         print(i)
    for i in range(len(num_stu)): #length of "num_stu" list
        
        tests.append(generateCase(i + 1, num_stu[i], course_lst[i])) 
        #course_lst IS A 3-D LIST.Indexing to this list is indexing to a 2-d list

    test_cases["tests"] = tests

    return test_cases


# In[64]:


test_cases = generateTestCases() 

with open('Conformity.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:





# In[ ]:




