#!/usr/bin/env python
# coding: utf-8

# Donny Histogram

# In[1]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
test1 = pd.read_csv('lab8_1.csv')
test1c = test1.iloc[:,2]
test2 = pd.read_csv('lab8_2_al.csv')
test2c = test2.iloc[:,2]
test3 = pd.read_csv('lab8_3_2al.csv')
test3c = test3.iloc[:,2]
test4 = pd.read_csv('lab8_4_3al.csv')
test4c = test4.iloc[:,2]
test5 = pd.read_csv('lab8_5_w.csv')
test5c = test5.iloc[:,2]
test6 = pd.read_csv('lab8_6_2w.csv')
test6c = test6.iloc[:,2]
test7 = pd.read_csv('lab8_7_3w.csv')
test7c = test7.iloc[:,2]
fig, ax = plt.subplots(figsize = (20,20), nrows = 7)
ax[0].hist(test1c)
ax[0].set_title('Sample Alone')
ax[1].hist(test2c)
ax[1].set_title('1 Aluminum sheet')
ax[2].hist(test3c)
ax[2].set_title('2 Aluminum sheets')
ax[3].hist(test4c)
ax[3].set_title('3 Aluminum sheets')
ax[4].hist(test5c)
ax[4].set_title('1 Tungsten sheet')
ax[5].hist(test6c)
ax[5].set_title('2 Tungsten sheet')
ax[6].hist(test7c)
ax[6].set_title('3 Tungsten sheet')


def m(input):
    print(np.mean(input))
def s(input):
    print(np.std(input))
print('Means:')
print('Sample:')
m(test1c)
print('1 aluminum:')
m(test2c)
print('2 aluminum:')
m(test3c)
print('3 aluminum:')
m(test4c)
print('1 tungsten:')
m(test5c)
print('2 tungsten:')
m(test6c)
print('3 tungsten')
m(test7c)

print('Standard Deviations:')
print('Sample:')
s(test1c)
print('1 aluminum:')
s(test2c)
print('2 aluminum:')
s(test3c)
print('3 aluminum:')
s(test4c)
print('1 tungsten:')
s(test5c)
print('2 tungsten:')
s(test6c)
print('3 tungsten')
s(test7c)


# Shahin Stats

# In[11]:


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


c1 = print(np.sum(new_data))
c2 = print(np.sum(new_data2))
c3 = print(np.sum(new_data3))
c4 = print(np.sum(new_data4))
c5 =print(np.sum(new_data5))
c6 =print(np.sum(new_data6))
c7 = print(np.sum(new_data7))


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


# In[12]:





# Error Bar stuff

# In[14]:


# Adjusting the code to directly use provided counts instead of calculating from initial values

# Placeholder values for demonstration, representing direct counts for various thicknesses
# These should be replaced with the actual counts if provided
counts = [379,  # Placeholder for np.sum(new_data) for 0 thickness
          93,  # Placeholder for np.sum(new_data2) for 1 cm Al
          110,  # Placeholder for np.sum(new_data3) for 2 cm Al
          76,   # Placeholder for np.sum(new_data4) for 3 cm Al
          43,  # Placeholder for np.sum(new_data5) for 1 cm W
          24,  # Placeholder for np.sum(new_data6) for 2 cm W
          11]   # Placeholder for np.sum(new_data7) for 3 cm W

# Custom thickness range to match provided counts
thickness_range_Al_W = [0, 1, 2, 3, 1, 2, 3]  # Matching counts to thicknesses for Al and W

# Labels for each data point
labels = ["No Absorber", "1 cm Al", "2 cm Al", "3 cm Al", "1 cm W", "2 cm W", "3 cm W"]

# Function to plot counts vs. thickness including uncertainties
def plot_counts_vs_thickness_direct(counts, thickness_range, labels):
    uncertainties = [math.sqrt(count) for count in counts]  # Assuming Poisson distribution for counts
    
    plt.figure(figsize=(10, 6))
    for i, label in enumerate(labels):
        plt.errorbar(thickness_range[i], counts[i], yerr=uncertainties[i], label=label, fmt='-o', capsize=5)
    
    plt.yscale('log')
    plt.xticks(range(4), ['0', '1 cm', '2 cm', '3 cm'])  # Adjusting x-ticks for clarity
    plt.xlabel('Absorber Thickness (cm)')
    plt.ylabel('Total Counts (with Uncertainties)')
    plt.title('Total Counts vs. Absorber Thickness (Direct Counts)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

# Calling the function with direct counts
plot_counts_vs_thickness_direct(counts, thickness_range_Al_W, labels)


# In[10]:





# Joey Coef math

# I = I0e^-ux (x = thickness)
# 
# Mean I0 = for 0 sheet => 31.58 Mean I Al = 1 sheet Al = 7.75 (1cm thick) Mean I W = 1 sheet W = 3.58 (1cm thick)
# 
# u(Al) = -ln(31.58/7.75)/1cm = -1.404 cm^-1
# 
# u(W) = -ln(31.58/3.58)/1cm = -2.177cm^-1
# 
# This makes sense as the Tungsten is more dense than Alumnium so its respective coefficent should be higher and as it is.

# In[ ]:




