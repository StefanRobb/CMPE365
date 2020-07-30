#!/usr/bin/env python
# coding: utf-8

# Search algorithms.
# @author Stefan Robb

# In[46]:


def Bin_Search(A,x):
    
    first = 0
    last = len(A) - 1
    count = 1
    
    while(first <= last):
        mid = int((first + last)/2)
        if A[mid] == x:
            return count
        elif A[mid] > x:
            last = mid - 1
        else:
            first = mid + 1
        count = count + 1
    return -1


# In[53]:


def Trin_Search(A,x):
    
    first = 0
    last = len(A) - 1
    count = 1
    
    while first <= last:
        t1 = int(first + (last - first)/3)
        if A[t1] == x:
            return t1
        elif A[t1] > x: # reduce to the first third
            last = t1 - 1
        else:
            first = t1 + 1
            if first > last:
                return -1
            mid = int((first + last)/2)
            if A[mid] == x:
                return count
            elif A[mid] > x: # reduce to the middle third
                last = mid - 1
            else:
                first = mid + 1 # reduce to the last third
        count = count + 1
    return -1


# In[95]:


A = []
size =  4000
for i in range(0,size):
    A.append(i)
x = 876
print(Bin_Search(A,x))
print(Trin_Search(A,x))

