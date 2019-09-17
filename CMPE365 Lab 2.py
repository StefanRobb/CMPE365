#!/usr/bin/env python
# coding: utf-8

# In[19]:


# open file as a 2d array and input source and destination
file = open(r"C:\Users\stefa\Desktop\Queens\Fourth Year\CMPE365\Labs\Lab 2\2019_Lab_2_flights_real_data.txt", "r")
linearray = []
for line in file:
    linearray.append([int(x) for x in line.split()])
cities = linearray[0][0]
del linearray[0]
length = len(linearray)
source = float('inf')
destination = float('inf')
while not source in range(0,cities):
    if source != float('inf'): print("Source city undefined, please enter a source city between 0 and " + str(cities - 1) + ".")
    source = int(input("Please enter your source city: ")) # source and destination must be less than number of cities
while not destination in range(0,cities):
    if destination != float('inf'): print("Destination city undefined, please enter a destination city between 0 and " + str(cities - 1) + ".")
    destination = int(input("Please enter your destination city: "))


# In[13]:


# initialize empty arrays
reached = []
estimate = []
candidate = []
predecessor = []


# In[14]:


# set initial conditions
for i in range(0,cities):
    reached.append(False)
    estimate.append(float('inf'))
    candidate.append(False)
    predecessor.append(source)
reached[source] = True
for i in range(0,length):
    if linearray[i][0] == source:
        candidate[linearray[i][1]] = True
        if linearray[i][3] < estimate[linearray[i][1]]:
            estimate[linearray[i][1]] = linearray[i][3]
estimate[source] = 0


# In[15]:


# Dijkstra's algorithm
while(not all(c == False for c in candidate)):
    best_candidate_estimate = float('inf')
    for i in range(0,cities):
        if candidate[i] == True and estimate[i] < best_candidate_estimate:
            v = i
            best_candidate_estimate = estimate[i]
    reached[v] = True
    candidate[v] = False
    for i in range(0,length):
        if linearray[i][0] == v and reached[linearray[i][1]] == False:
            if linearray[i][3] < estimate[linearray[i][1]] and estimate[linearray[i][0]] < linearray[i][2]:
                estimate[linearray[i][1]] = linearray[i][3]
                candidate[linearray[i][1]] = True
                predecessor[linearray[i][1]] = v


# In[16]:


# print output
if estimate[destination] != float('inf'):
    pre = destination
    path = []
    path.append(pre)
    print("Optimal route from " + str(source) + " to " + str(destination) + "\n")
    while(pre != source):
        pre = predecessor[pre]
        path.append(pre)
    path = list(reversed(path))
    for i in range(0,len(path) - 1):
        print("Fly from " + str(path[i]) + " to " + str(path[i+1]))

    print("\nArrive at " + str(destination) + " at time " + str(estimate[destination]))
else:
    print("No available path")

