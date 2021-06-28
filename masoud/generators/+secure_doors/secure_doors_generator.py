#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import random
from random import choice
import names


# In[8]:


def generateNumbers():#generating input numbers

    random.seed(500)

    entry_names_lst = []

    # a list with 50 elem each for number of entery for each samp
    num_entery = [random.randint(1, 1000) for _ in range (50)] 
    
    #making a list of entry names lists with different length (random in range "num_entery")
    for i in range(50):
           #making 50 lists of entry sentences nested in another list
            entry_names_lst.append([str(choice([" entry " , "exit "])) 
            + (names.get_first_name()) for _ in range (num_entery[i]) ]) 

    return num_entery, entry_names_lst


# In[7]:


# print(generateNumbers())


# In[12]:


# generating a dic containing case, input, and result strings 
def generateCase(case, num_entery, entry_names_lst):

    new_case = {}
    already_entered_names_lst = []
    
    new_case["case"] = case
    new_case["input"] = str(num_entery) + " " + " ".join(entry_names_lst)
    new_case["output"] = []
    
    for word in entry_names_lst:
        if (word.startswith("entry")):
            if (word.split(' ')[1] in already_entered_names_lst):
                new_case["output"].append(word.split(' ')[1] + " entered" + " (ANOMALY)") 
            else:
                already_entered_names_lst.append(word.split(' ')[1])
                new_case["output"].append(word.split(' ')[1] + " entered") # Get 2nd word in String

        elif (word.startswith("exit")):
            if (word.split(' ')[1] not in already_entered_names_lst):
                new_case["output"].append(word.split(' ')[1] + " exited" + " (ANOMALY)") 
            else:
                already_entered_names_lst.remove(word.split(' ')[1])#I need to removed the name from the entry_names_lst
                new_case["output"].append(word.split(' ')[1] + " exited")# Get 2nd word in String
 

    return new_case


# In[14]:


def generateTestCases(): #generating 50 test cases

  num_entery, entry_names_lst = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(len(num_entery)):
    tests.append(generateCase(i + 1, num_entery[i], entry_names_lst[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases() 

with open('secure_doors.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




