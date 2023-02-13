#!/usr/bin/env python
# coding: utf-8

# ![icon](https://th.bing.com/th/id/OIP.c_p8Fa-MeQ6DONik_FuopQHaFw?w=200&h=180&c=7&r=0&o=5&dpr=1.1&pid=1.7)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('/kaggle/input/udemy-courses-revenue-generation-and-course-anal/Entry Level Project Sheet - 3.1-data-sheet-udemy-courses-web-development.csv')


# ### Get some information about data

# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.sample()


# In[6]:


df.describe()


# ## Cleaning data

# In[7]:


df.isna().sum()


# In[8]:


df.dropna(inplace=True)


# In[9]:


df[df.duplicated()]


# In[10]:


df.duplicated()


# In[11]:


df.drop_duplicates(inplace=True)


# In[12]:


df.drop('url',axis=1,inplace=True)


# ### Convert object to date
# #### convert data that on left and but it in the main column

# In[13]:


df ['published_timestamp'] = pd.to_datetime(df ['published_timestamp']).dt.date


# In[14]:


df.drop('course_id',axis=1,inplace=True)


# In[15]:


df.head()


# ____________
# ## visualize 
# * ### we will start with categorcal data
# * ### find relation between columns

# In[16]:


sns.countplot(x='Free/Paid',data=df,palette="terrain_r")
plt.title('paid vs free courses')


# In[17]:


df['Free/Paid'].value_counts()


# In[18]:


#plt.figure(figsize=(6,5))
sns.countplot('level',data=df,palette="terrain_r")
plt.title('Comparison between levels')


# In[19]:


plt.figure(figsize=(10,5))
sns.countplot('subject',data=df,palette="terrain_r")


# In[20]:


df['subject'].value_counts()


# ### ---> most requirment in courses is Web Development and Business Finance

# In[21]:


#corr=corrilation in math like relation if it was negative that mean Reverse
#if was possitive that mean Expel
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(),annot=True)


# ### subscriber vs price

# In[22]:


plt.figure(figsize=(8,6))
sns.regplot(x='price',y='num_subscribers',data=df)


# In[23]:


#num_reviews vs price
plt.figure(figsize=(8,6))
sns.regplot(x='price',y='num_reviews',data=df)


# In[24]:


plt.figure(figsize=(8,6))
sns.regplot(x='price',y='content_duration',data=df)


# 

# In[25]:


plt.figure(figsize=(8,6))
sns.regplot(x='num_subscribers',y='content_duration',data=df)


# ### --> contenent duration leads to more subscribers

# # Conclusions
# #### most of the courses paid
# #### most of the courses is for all levels or biginner level
# #### price didn't affect on num_reviews
# #### subsccriber didn't effict on price
# #### content_duration may affect on price

# ### 
