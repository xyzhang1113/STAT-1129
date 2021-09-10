#!/usr/bin/env python
# coding: utf-8

# In[55]:


colors = ["pink","red","green","blue","white"]


# In[56]:


nums = list(range(30,63,3))
print(nums)


# In[57]:


nums1 = tuple(nums)
nums1 = (30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60)
print(nums1)


# In[58]:


#empty list
empty_list = []


# In[59]:


for number in range(0, 6):
    empty_list += [number]
print(empty_list)


# In[60]:


del empty_list[2]
print(empty_list)


# In[61]:


empty_list.insert(2,2.0)
print(empty_list)


# In[62]:


print(len(empty_list))
print(max(empty_list))
print(min(empty_list))


# In[63]:


nums2 = list(range(1,11))
print(nums2)


# In[64]:


nums2[0]+nums2[1]+nums2[2]+nums2[3]+nums2[4]+nums2[5]+nums2[6]+nums2[7]+nums2[8]+nums2[9]

