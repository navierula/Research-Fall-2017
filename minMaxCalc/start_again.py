#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:06:12 2017

@author: navrajnarula
"""

#c = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112, 108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]
#c= [0, 10, 11, 48, 50.5, 0.48, 17, 18, 23, 29, 33, 34.67, 50.1, 0.09, 7, 41, 45, 50]

#### METHOD 1: Create generator function

lst = [-0.5, 44, 90, 132.22, 129.6, 89, 67.91, 12.5, 11, 0.0006, 10.2,
    67, 89.07, 100, 132.224, 129.88, 120.1, 100, 89.5, 75, 40, 9.8, -0.4,
    0.1, 90, 99, 112, 132.22,
]

def get_groups(lst):
    up = False
    for i, (u, v) in enumerate(zip(lst, lst[1:])):
        if up:
            if v < u:
                yield 'End', i, u
                up = False
        else:
            if v > u:
                yield 'Start', i, u
                up = True
    if up:
        yield 'End', i + 1, lst[-1]

#print("METHOD 1:\n")
#for t in get_groups(lst):
#    print(t)
    
#### METHOD 2: using numpy libraries
from scipy.signal import argrelextrema
import numpy as np 

lst = [-0.5, 44, 90, 132.22, 129.6, 89, 67.91, 12.5, 11, 0.0006, 10.2, 67, 89.07, 100, 132.224, 129.88, 120.1, 100, 89.5, 75, 40, 9.8, -0.4, 0.1, 90, 99, 112, 132.22]
arr = np.array(lst)

#Find local minimas index, add zero in the beginning
minInd = np.insert(argrelextrema(arr, np.less),0,0)
# Find local maximas index, add the length of arr - 1 at the end 
maxInd = np.append(argrelextrema(arr,np.greater),[len(lst)-1])

# numpy indexing and zip to combine the results
end_arr = list(zip(zip(minInd,arr[minInd]),zip(maxInd,arr[maxInd])))

##Printing the output
#print("\nMETHOD 2:\n")
#for i in end_arr:
#    print('Start :' , i[0])
#    print('End:', i[1],'\n')
    
#### METHOD 3: Sorting
    
load = lst
    
load.sort(key=float) # previously key = int

totals = []

for count, items in enumerate(load):

    counter = count + 1
    last_object = (counter, load[count], load[(len(load)-1) - count])

    totals.append(last_object)
    
#our_totals = totals[:3]
#print("\nMETHOD 3:\n")
#print(our_totals)

###############################################
print("\nTrying on REAL data:\n")

import pandas as pd

# read in dataset
xl = pd.ExcelFile("data/130N_Cycles_1-47.xlsx")
df = xl.parse("Specimen_RawData_1")
df

# append data from load column to list
load = []
for item in df.index:
    load.append(df["Round"][item])

    
#### METHOD 1: Create generator function

lst = load

def get_groups(lst):
    up = False
    for i, (u, v) in enumerate(zip(lst, lst[1:])):
        if up:
            if v < u:
                yield 'End', i, u
                up = False
        else:
            if v > u:
                yield 'Start', i, u
                up = True
    if up:
        yield 'End', i + 1, lst[-1]

print("METHOD 1:\n")
for t in get_groups(lst):
    print(t)
#### METHOD 2: using numpy libraries
from scipy.signal import argrelextrema
import numpy as np 

lst = load
arr = np.array(lst)

#Find local minimas index, add zero in the beginning
minInd = np.insert(argrelextrema(arr, np.less),0,0)
# Find local maximas index, add the length of arr - 1 at the end 
maxInd = np.append(argrelextrema(arr,np.greater),[len(lst)-1])

# numpy indexing and zip to combine the results
end_arr = list(zip(zip(minInd,arr[minInd]),zip(maxInd,arr[maxInd])))

#Printing the output
#print("\nMETHOD 2:\n")
#count = 0
#for i in end_arr:
#    if count <= 47:
#        print('Start :' , i[0])
#        print('End:', i[1],'\n')
#        count += 1
    
#### METHOD 3: Sorting

    
load.sort(key=float) # previously key = int

totals = []

for count, items in enumerate(load):

    counter = count + 1
    last_object = (counter, load[count], load[(len(load)-1) - count])

    totals.append(last_object)
    
#our_totals = totals[:47]
#print("\nMETHOD 3:\n")
#print(our_totals)
    
# save the output in the list, min and the max
# run it through my algorithm 
# compare them separately in algorithm
    
# save rows in file --> rounding to 0 helps
# play with rounding to comma 1,
# compare it with the real data
# check both minimin and maximum
# do it manually for 2 - 3 different ones
# clean the data from all bad values
# use ROUND, not anything else!!!
    
# redownloaded dataset
