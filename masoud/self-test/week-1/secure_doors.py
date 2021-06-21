#!/usr/bin/env python
# coding: utf-8

# ## Sudo code
# * input a number between 1 and 100 (including) as the length of the log
# 
# * input a list of n strings in the form of "entry name" or "exit name" (name is up to 20 upper /lower characters)
# 
# * for every element of list if it starts with entry print "name entered", elif it starts with exit print "name exited"
# 
# if it already entered and enter again add "(ANOMALY)"
# making a list of all names alreay entered
# if it has not entered before and exits, add "(ANOMALY)"
# 

# In[10]:


n = int(input()) #input length of the log


lst = [] #making an empty list
entry_names_lst = []

for i in range (n): #inputing elements of list
    
    ele = input()
    lst.append(ele)
    
    
for word in lst:
    if (word.startswith("entry")):
        if (word.split(' ')[1] in entry_names_lst):
            print(word.split(' ')[1] + " entered" + " (ANOMALY)")
        else:
            entry_names_lst.append(word.split(' ')[1])
            print(word.split(' ')[1] + " entered")# Get 2nd word in String
        
    elif (word.startswith("exit")):
        if (word.split(' ')[1] not in entry_names_lst):
            print(word.split(' ')[1] + " exited" + " (ANOMALY)")
        else:
            entry_names_lst.remove(word.split(' ')[1])#I need to removed the name from the entry_names_lst
            print(word.split(' ')[1] + " exited")# Get 2nd word in String


# In[ ]:




