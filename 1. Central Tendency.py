#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Central Tendency

# In[5]:


#randint will generate random integer values
#10 se shuru krke 17 tak and 5 random numbers in between
m = np.random.randint(10,17,5)
print(m)


# ## Mean

# Mean is the sum of the value of each observation in a dataset divided by no. of observations

# In[7]:


np.mean(m)


# ## Median

# In[12]:


#To find median, we need to keep array in ascending order
median_ascend = np.sort(m)
print(median_ascend)
#finding median
np.median(median_ascend)


# ## Mode

# In[14]:


#we do not have mode method in numpy, so we will import this from statistic
from statistics import mode
mode(m)


# # Population and Sample

# In[15]:


population = np.random.randint(10,20,100)
population


# In[16]:


np.mean(population)


# In[17]:


np.median(population)


# In[18]:


from statistics import mode
mode(population)


# # Sample
# Sample is a subset of population

# In[20]:


#basically we are chosing any no. from population to make it as our sample and numbers in sample will be 20
sample = np.random.choice(population,20)
sample


# In[22]:


np.mean(sample)


# In[27]:


sort = np.sort(sample)
print(sort)
np.median(sort)


# In[28]:


from statistics import mode
mode(sort)


# In[31]:


sample_1 = np.random.choice(population,10) 
sample_2 = np.random.choice(population,10) 
sample_3 = np.random.choice(population,10) 
sample_4 = np.random.choice(population,10) 


# In[32]:


all_sample = [sample, sample_1, sample_2, sample_3, sample_4]
sample_mean=[]

for i in all_sample:
    sample_mean.append(np.mean(i))

sample_mean


# In[33]:


np.mean(sample_mean)

