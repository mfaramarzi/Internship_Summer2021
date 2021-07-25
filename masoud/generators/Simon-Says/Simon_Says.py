#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random


# In[2]:


def generateNumbers():#generating input numbers

    random.seed(500)

    num_lines = [random.randint(1, 20) for _ in range (50)]
    
#     writing a sentence which randomly may start with a specific words
        
        # why used tuples not list?
    nouns = ("puppy", "car", "rabbit", "simon", "simon")
    verbs = ("runs", "hits", "jumps", "says", "says") 
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")

    l=[nouns,verbs,adj,adv] #list of tuples
    
    all_sentences = []
        
    for i in range (50):
        
        #list comprehension
        all_sentences.append([' '.join([random.choice(j) for j in l])
                              for k in range (num_lines[i])])

    return num_lines, all_sentences


# In[3]:


# generateNumbers()


# In[4]:


def generateCase(case, num_lines, all_sentences):# generating a dic containing case, input, and result strings 

    new_case = {}

    new_case["case"] = case
    
    new_case["input"] = str(num_lines)
    
    for i in range (len(all_sentences)):
    
        new_case["input"] = new_case["input"] + "\n" + all_sentences[i]
        
    new_case["output"] = ""
    
    for i in range (len(all_sentences)):
        
    #     if sentence does not start with "simon says", print empty line
    # else print the rest of sentence

        if (all_sentences[i].startswith("simon says")):

    #splitting stence by space and slicing from index 2 to the end
            command_sent = ""
        
            splitted_sent = all_sentences[i].split(" ")

            command_sent += " " .join(splitted_sent[2:])

            new_case["output"] = new_case["output"] + "\n" + command_sent

        else:

            new_case["output"] = new_case["output"] + "\n" + ""
            
    new_case["output"] = new_case["output"].strip()

    return new_case


# In[5]:


def generateTestCases(): #generating 50 test cases

    num_lines, all_sentences = generateNumbers()

    test_cases = {}
    
    tests = []
    
    for i in range(len(num_lines)):
        
        tests.append(generateCase(i + 1, num_lines[i], all_sentences[i]))

    test_cases["tests"] = tests

    return test_cases


# In[6]:


test_cases = generateTestCases() 


# In[7]:


with open('Simon_Says.json', 'w') as json_file:
    
    json.dump(test_cases, json_file, indent = 4, sort_keys = True)


# In[ ]:




