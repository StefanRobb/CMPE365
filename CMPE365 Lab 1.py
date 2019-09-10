#!/usr/bin/env python
# coding: utf-8

# In[ ]:


file = open(r"C:\Users\stefa\Desktop\Queens\Fourth Year\CMPE365\Dijkstra_Data_1600.txt", "r")
linearray = []
for line in file:
    linearray.append([int(x) for x in line.split()])
len = linearray[0][0]
print(len)
del linearray[0]
cost = []
reached = []
estimate = []
candidate = []
predecessor = []
for i in range(0,len):
    reached.append(False)
    estimate.append(0)
    candidate.append(False)
    predecessor.append(0)
    cost.append(0)
    if i == 0:
        reached[i] = True
        cost[i] = 0
    if linearray[0][i] != 0:
        estimate[i] = weight(0,i)
        candidate[i] = True
    else:
        estimate[i] = float('inf')
        candidate[i] = False
estimate[0] = 0
for i in range(0,len):
    best_candidate_estimate = float('inf')
    for x in range(1, len):
        if candidate[x] == True and estimate[x] < best_candidate_estimate:
            v = x
            best_candidate_estimate = estimate[x]
    cost[v] = estimate[v]
    reached[v] = True
    candidate[v] = False
    for y in range(0, len):
        if weight(v,y) > 0 and reached[y] == False:
             if cost[v] + weight(v,y) < estimate[y]:
                estimate[y] = cost[v] + weight(v,y)
                candidate[y] = True
                predecessor[y] = v
print(estimate.index(max(estimate)))


# In[43]:


def weight(a,b):
    return linearray[a][b]


# In[45]:


def finishtest(estimate):
    for e in estimate:
        if e == float('inf'):
            return True
    return False

