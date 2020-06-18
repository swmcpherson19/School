# -*- coding: utf-8 -*-
"""
@author: swmcpherson
"""
# Determine start time
import time
start = time.time()

# Data Set 10:
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180

# Custom function to add a column in the list that computes the overall weight ratio of the item
def load(items,cap):
    item_list = [[i,w,v] for i,w,v in items]
    
    for i in range(len(item_list)):
        item_list[i].append(item_list[i][1]/cap)
    j = lambda x:x[3]
    item_list=sorted(item_list,key=j,reverse=True)

    return item_list

# Object created after function is created
knapsack=load(items,cap)

# Objects for reporting
totalwt = 0
totalval = 0
current = 0
knap=[]

# Loop that loads knap if the weight is under capacity.  If that item won't fit, 
# it moves on to the next object
for i in range(len(knapsack)):
    if current + knapsack[i][1] <= cap:
            current += knapsack[i][1]
            knap.append(knapsack[i])
    elif current + knapsack[i][1] > cap:
            continue
# Loop that fills in the reporting objects   
for i in range(len(knap)):
    items=[]
    items.append(knap[i][0])
    totalwt += knap[i][1]
    totalval += knap[i][2]

# Printout sections
print('swmcpherson')
print("Knapsack contains the following items\n  " +
     '\n  '.join(sorted(item for item,_,_,_ in knap)))
print("For a total value of %i and a total volume of %i" % (totalwt, totalval))

# Determine ending time
end = time.time()

#Print total time.
print("For a total time in seconds of ")
print(end - start)





