#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:02:19 2017
@author: navrajnarula

During our discussion last time, we came to the conclusion that the dataset
itself oscillates. Because of this, min and max values returned are not the actual
min and max values they should be.

Our solution to fix this issue is to experiment with rounding in the Excel 
document. We will use the ROUND function in Excel to round 0 and round 1.
Then, we will run the results and see what happens with my current algorithm.
"""

import pandas as pd

# read in dataset
xl = pd.ExcelFile("data/130N_Cycles_1-47.xlsx")
df = xl.parse("Specimen_RawData_1")

# append data from time column to list
time = []
for item in df.index:
    time.append(df["Time"][item])

# append data from load column to list
load = []
for item in df.index:
    load.append(df["Load"][item])

# append data from round zero column to list
round_zero = []
for item in df.index:
    round_zero.append(df["Round_Zero"][item])
    
# append data from round one column to list
round_one = []
for item in df.index:
    round_one.append(df["Round_One"][item])
 
# define generator function to determine start 
# and end points for min and max values
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

# append all returned values to a list
points = []
for t in get_groups(round_zero):
    points.append(t)
  
# assign result get_groups to variable
gen = get_groups(round_zero)

mins = []
maxes = []
max_ = []
for i, (t1, t2) in enumerate(zip(gen, gen), 1):
    mins.append((i, t1[1],t1[2]))
    maxes.append((t2[1],t2[2]))
    max_.append(t2[2])
    
# append max values to list and see if they correspond to actual MAX values!!
pointss = []
for t in get_groups(maxes):
    pointss.append(t)
    
# define generator function to determine start 
# and end points for min and max values
def get_groups(lst):
    up = False
    for i, (u, v) in enumerate(zip(lst, lst[1:])):
        if up:
            if v[1] < u[1]:
                yield 'End', i, u[0], u[1]
                up = False
        else:
            if v[1] > u[1]:
                yield 'Start', i, u[0], u[1]
                up = True
    if up:
        yield 'End', i + 1, lst[-1]
        
gen = get_groups(maxes)

final_min_max = []
for i, (t1, t2) in enumerate(zip(gen, gen), 1):
    final_min_max.append((t1,t2))

# proceed with next steps

# 1) combine data
# 2) total time for each cycle
# 3) total heating time for each cycle
# 4) total cooling time for each cycle

# combine data only with min and max labels,
# THEN, append time    
combine_data = []
for i in range(len(load)):
    flag = 0
    for j in final_min_max:
        if i == j[0][2]:
            combine_data.append((load[i], "min"))
            flag = 1
        if i == j[1][2]:
            combine_data.append((load[i], "max"))
            flag = 1
    if flag == 0:
        combine_data.append((load[i], "NA"))
    
# combine data with time
data_with_time = []
for i, j in zip(time, combine_data):
    data_with_time.append((i,) +j)
    


