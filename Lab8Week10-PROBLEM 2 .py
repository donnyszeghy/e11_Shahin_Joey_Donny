#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import math 


# In[10]:


d1 = pd.read_csv("lab8_1.csv")
d2 = pd.read_csv("lab8_2_al.csv")
d3 = pd.read_csv("lab8_3_2al.csv")
d4 = pd.read_csv("lab8_4_3al.csv")
d5 = pd.read_csv("lab8_5_w.csv")
d6 = pd.read_csv("lab8_6_2w.csv")
d7 = pd.read_csv("lab8_7_3w.csv")


new_data = d1.loc[:,"Counts"]
new_data2 = d2.loc[:,"Counts"]
new_data3 = d3.loc[:,"Counts"]
new_data4 = d4.loc[:,"Counts"]
new_data5 = d5.loc[:,"Counts"]
new_data6 = d6.loc[:,"Counts"]
new_data7 = d7.loc[:,"Counts"]




# In[3]:


print(np.mean(new_data))
print(np.mean(new_data2))
print(np.mean(new_data3))
print(np.mean(new_data4))
print(np.mean(new_data5))
print(np.mean(new_data6))
print(np.mean(new_data7))


# We can see that roughly that as we increased the amount and stregth of shielding of the material that the mean number of counts recorded in our time interval decreased
# 

# In[4]:


print(np.std(new_data))
print(np.std(new_data2))
print(np.std(new_data3))
print(np.std(new_data4))
print(np.std(new_data5))
print(np.std(new_data6))
print(np.std(new_data7))


# In addition we can see that as we increase the thickness and shielding strength our std decreases as our counts are decreasing, we can see this through the uncertainity in the next step

# In[5]:


print(np.sum(new_data))
print(np.sum(new_data2))
print(np.sum(new_data3))
print(np.sum(new_data4))
print(np.sum(new_data5))
print(np.sum(new_data6))
print(np.sum(new_data7))


# In[9]:


print(math.sqrt((np.sum(new_data))))
print(math.sqrt((np.sum(new_data2))))
print(math.sqrt((np.sum(new_data3))))
print(math.sqrt((np.sum(new_data4))))
print(math.sqrt((np.sum(new_data5))))
print(math.sqrt((np.sum(new_data6))))
print(math.sqrt((np.sum(new_data7))))


# We can see the Uncertainties are generally greater than the standard deviations observed from our data because we only ran this experiment a single time. Yes we have large count values, but our uncertainity range is much bigger as we only are going off of matching this data to a poisson distribtuion. This is why our std measurements are so much less because they fit inside the uncertainity we are allowed to have. 

# Generally we see that as the thickness of the material increases then the number of counts decreases, with the exception of one trial which most likely had an error in distance to detector. This is proved in the equation we are given which shows that as material thickness increases the Counts per min decrease I1 = I0 (e^-ut)

# In[ ]:




