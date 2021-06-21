#!/usr/bin/env python
# coding: utf-8

# ## Input
# The number of classes, number of students in each class and their final grades
# 
# ## Ouput
# Percentage of studets in ach class with final grade above ave of class

# In[26]:


NumClasses = int(input())
class_grades = []
above_ave_grades = []


# In[27]:


for i in range (NumClasses):
    
    NumStudents = int(input())
    
    for j in range (NumStudents):
        
        class_grades.append(int(input()))
        
    ave = (sum(class_grades) / len(class_grades))
#     print(ave)
    
    for j in class_grades:
        
        if (j > ave):
            
            above_ave_grades.append(j)
        
    percent = (len(above_ave_grades) / len(class_grades) ) * 100
    
    formatted_percent = "{:.3f}".format(percent)
    
    print(formatted_percent , "%")
            


# In[ ]:




