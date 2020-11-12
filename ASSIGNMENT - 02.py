#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question1
list = []
newlist = []
for i in range(10):
    list.append(input())
    if int(list[i]) % 2 == 0:
        newlist.append(list[i])
print(newlist)


# In[2]:


# Question2
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example: You want to create a list of all the fruits that has the letter "a" in the name.


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[3]:


# Question 3

d=dict()
n = int(input())
for x in range(1,n+1):
    d[x]=x**2
print(d)  


# In[4]:


# Question 4

import math
pos = [0,0]
n = int(input())
for i in range(n):
    s = input()
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[1]+=steps
    elif direction=="DOWN":
        pos[1]-=steps
    elif direction=="LEFT":
        pos[0]-=steps
    elif direction=="RIGHT":
        pos[0]+=steps
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))


# In[ ]:




