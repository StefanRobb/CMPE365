#!/usr/bin/env python
# coding: utf-8

# In[33]:


import math
import statistics
import random
import matplotlib.pyplot as plt

# create set class
class Set:
    def __init__(self, initial_list = []):
        self.elements = initial_list
        self.sum = sum(self.elements)
        
# test part 1        
S = Set([10,20,30])
k = 20
BFI_Subset_Sum(S,k)
HS_Subset_Sum(S,k)


# In[34]:


# generate experimental data for part 2
BFI_op_av = []
HS_op_av = []
for n in range(4,15):
    BFI_n_av = []
    HS_n_av = []
    for i in range(1,20):
        random_list = []
        random_target = []
        BFI_set_ops = []
        HS_set_ops = []
        BFI_n_ops = []
        HS_n_ops = []
        S = Set(random.sample(range(1,101), n)) # creates a random list of size n
        subsets, count = Modified_BFI_SubsetandSums(S)
        subset_sums = []
        for ss in subsets:
            subset_sums.append(ss.sum)
        target_sums = random.sample(subset_sums, 10) # creates a random list of subset sums
        
        #perform the experiment
        for k in target_sums:
            BFI_count = BFI_Subset_Sum(S,k)
            HS_count = HS_Subset_Sum(S,k)
            BFI_set_ops.append(BFI_count)
            HS_set_ops.append(HS_count)
        BFI_set_av = statistics.mean(BFI_set_ops)
        HS_set_av = statistics.mean(HS_set_ops)
        BFI_n_ops.append(BFI_set_av)
        HS_n_ops.append(HS_set_av)
    BFI_n_av = statistics.mean(BFI_n_ops)
    HS_n_av = statistics.mean(HS_n_ops)
    BFI_op_av.append(BFI_n_av)
    HS_op_av.append(HS_n_av)


# In[35]:


# Create plot
BFI_data = (range(4,15), BFI_op_av)
HS_data = (range(4,15), HS_op_av)
data = (BFI_data, HS_data)
colors = ("red", "green")
groups = ("BFI Operations", "HS Operations")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.title('Scatter plot of operation count for subset sum methods')
plt.xlabel('Number of elements in set')
plt.ylabel('Number of operations to find subset sum')
plt.show()


# In[25]:


def BFI_Subset_Sum(S,k):
    count = 0
    subsets = []
    empty_set = Set()
    subsets.append(empty_set)
    count += 3
    
    for i in range(0,len(S.elements)):
        new_subsets = []
        count += 1
        for old_u in subsets:
            new_u = Set(old_u.elements + [S.elements[i]])
            count += len(old_u.elements) + 1 # copying a list is O(n)
            if new_u.sum == k:
                print("new_u: " + str(new_u.elements) + " is a solution")
                count += 2 # verify if and print if true
                return count
            else:
                new_subsets.append(old_u)
                new_subsets.append(new_u)
                count += 3 # verify if and 2 appends
        subsets = new_subsets
        count += len(subsets) # copy list

    print("No solution")
    return count


# In[2]:


def HS_Subset_Sum(S,k):
    count = 0
    S_left = Set((S.elements[0:int(len(S.elements)/2)]))
    S_right = Set((S.elements[int(len(S.elements)/2):len(S.elements)]))
    count += len(S.elements) # creating new sets total n elements
    left_sets, left_ops = Modified_BFI_SubsetandSums(S_left)
    right_sets, right_ops = Modified_BFI_SubsetandSums(S_right)
    left_subsets = []
    left_sums = []
    right_subsets = []
    right_sums = []
    count += 4 # initialize 4 empty arrays
    
    #create left and right corresponding subset and sums lists
    for ls in left_sets:
        left_subsets.append(ls.elements)
        left_sums.append(ls.sum)
        count += 2
    for rs in right_sets:
        right_subsets.append(rs.elements)
        right_sums.append(rs.sum)
        count += 2

    # if k is in left or right subsets else use pair sum
    if k in left_sums:
        print(str(left_subsets[left_sums.index(k)]) + " in left subset")
        count += 2
        return left_ops + right_ops + count
    elif k in right_sums:
        print(str(right_subsets[right_sums.index(k)]) + " in right subset")
        count += 2
        return right_ops + left_ops + count
    else:
        ltemp_sums = list(left_sums)
        rtemp_sums = list(right_sums)
        count += len(left_sums) + len(right_sums)
        ltemp_sums.sort()
        rtemp_sums.sort()
        lsort_time = 3*len(ltemp_sums)*math.log2(len(ltemp_sums))
        rsort_time = 3*len(rtemp_sums)*math.log2(len(rtemp_sums))
        a, b, sum_ops = Pair_Sum(ltemp_sums, rtemp_sums, k)
        if a != -1 and b != -1: # if a solution was found retrace steps to find corresponding subsets
            print(str(left_subsets[left_sums.index(ltemp_sums[a])]) + " and " + str(right_subsets[right_sums.index(rtemp_sums[b])]))
            count += 5
            return left_ops + right_ops + lsort_time + rsort_time + sum_ops + count
        else:
            print("No subset sums to the target value")
            count += 1
            return left_ops + right_ops + lsort_time + rsort_time + sum_ops + count
        


# In[3]:


def Modified_BFI_SubsetandSums(S):
    count = 0
    subsets = []
    empty_set = Set()
    subsets.append(empty_set)
    count += 3
    
    for i in range(0,len(S.elements)):
        new_subsets = []
        count += 1
        for old_u in subsets:
            new_u = Set(old_u.elements + [S.elements[i]])
            new_subsets.append(old_u)
            new_subsets.append(new_u)
            count += len(old_u.elements) + 3
        subsets = new_subsets
        count += 1
        
    return (subsets, count)


# In[4]:


def Pair_Sum(values1, values2, k):
    count = 0
    p1 = 0
    p2 = len(values2) - 1
    count += 2
    
    while(p1 <= len(values1) - 1 and p2 >= 1):
        t = values1[p1] + values2[p2]
        count += 3
        if t == k:
            count += 1
            return (p1,p2, count)
        elif t < k:
            p1 += 1
            count += 2
        else:
            p2 -= 1
            count += 1
            
    return (-1,-1, count)

