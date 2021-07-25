#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
import random
import statistics


# In[22]:


def generateNumbers():#generating input numbers

    random.seed(500)

    first_numbers = [random.randint(1, 100) for _ in range (50)]
    
    second_numbers = [random.randint(1, 100) for _ in range (50)]
    
    third_numbers = [random.randint(1, 100) for _ in range (50)]
    
    lst_letters = ["A" , "B" , "C"] #list of alphabetes
    
    lst_letters_50 = []
    
    #50 shuffled lists of lst_letters
    for _ in range(50):
        
        random.shuffle(lst_letters)
        
        lst_letters_50.append(list(lst_letters))
        
#     [[lst_letters_50.append(random.shuffle(lst_letters))] for _ in range(50)]

    return first_numbers, second_numbers, third_numbers, lst_letters_50


# In[23]:


generateNumbers()


# In[33]:


def generateCase(case, first_numbers, second_numbers, third_numbers, lst_letters_50):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = "%d %d %d" % (first_numbers, second_numbers, third_numbers)
    
    new_case["input"] = new_case["input"] + "\n" + "".join(lst_letters_50)
    
#     my code
    
    final_lst = []
    
    lst_nums = [first_numbers, second_numbers, third_numbers]
    
    my_dic = {"A" : min(lst_nums), "B" : statistics.median(lst_nums), "C" : max(lst_nums)}
    
    for i in lst_letters_50:
        
        final_lst.append(my_dic[i])
    
    new_case["output"] = "%d %d %d" %(final_lst[0], final_lst[1], final_lst[2])

    return new_case


# In[34]:


def generateTestCases(): #generating 50 test cases

    first_numbers, second_numbers, third_numbers, lst_letters_50 = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(first_numbers)):
        
        tests.append(generateCase(i + 1, first_numbers[i], second_numbers[i], third_numbers[i], lst_letters_50[i]))

    test_cases["tests"] = tests

    return test_cases


# In[35]:


test_cases = generateTestCases() 


# In[36]:


with open('ABC.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




