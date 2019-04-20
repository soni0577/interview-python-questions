#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = list(input('Enter the list of char : '))


# In[2]:


l


# In[3]:


first_l_ascii = []


# In[4]:


for i in l:
    first_l_ascii.append(ord(i))


# In[5]:


first_l_ascii


# In[6]:


rev_first = first_l_ascii[::-1]


# In[7]:


rev_first


# In[8]:


len(rev_first)


# In[9]:


f_sub_list = []


# In[10]:


for i in range(len(rev_first)-1):
        sub_1 = abs(rev_first[i]-rev_first[i+1])
        f_sub_list.append(sub_1)


# In[11]:


f_sub_list


# In[12]:


first_l_ascii


# In[13]:


s_sub_list = []


# In[14]:


for i in range(len(first_l_ascii)-1):
    sub_2 = abs(first_l_ascii[i]-first_l_ascii[i+1])
    s_sub_list.append(sub_2)


# In[15]:


s_sub_list


# In[16]:


sorted(s_sub_list)


# In[17]:


sorted(f_sub_list)


# In[18]:


if sorted(f_sub_list) == sorted(s_sub_list):
    print('funny')
else:
    print('not funny')


# In[ ]:




