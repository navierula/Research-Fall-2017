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
    
# calculate time for each cycle
it = iter(data_with_time)

out = []
ap = [next(it)[0]]
for e,_,state in it:
    if state == 'min':
        out.append(ap)
        ap = []
    ap += [e]
out.append(ap)

final_times = []
for item in out:
    final_times.append(item[-1]-item[0])
    
final_times = final_times[1:]
    
#########################
min_lst = []
max_lst = []
for item in combine_data:
    if item[1] == "min":
        min_lst.append(item[0])
    if item[1] == "max":
        max_lst.append(item[0])
#########################
    
lst = data_with_time

low_lst = []
high_lst = []

STATE = None
state_dict = {'min': low_lst, 'max': high_lst}

for x, y, z in lst:
    if z=='min' or z=='max':
        STATE = z
        sublist = []
        state_dict[STATE].append(sublist)
        sublist.append(x)
    if STATE and z=='NA':
        sublist.append(x)

###############################################
    
data_ = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]


# heating time
low_res = []
for item in low_lst:
    low_res.append(item[-1]-item[0])
    
high_res = []
for item in high_lst:
    high_res.append(item[-1]-item[0])
    
###########
cycles = []
for i in range(1,48):
    cycles.append(i)
##########
    
"""
cycles - list of cycle numbers
max_lst - maximum value
min_lst - minimum value
final_times - total time for each cycle
high_res - cooling time
low_res - heating time
"""

final = []
for a, b, c, d, e, f in zip(cycles, min_lst, max_lst, final_times, high_res, low_res):
    final.append((a,b,c,d,e,f))


with open("final.txt", "w") as fp:
    for item in final:
        fp.write("Cycle: %s" % str(item[0]) + "\n")
        fp.write("Minimum value: %s" % str(item[1]) + "\n")
        fp.write("Maximum value: %s" % str(item[2]) + "\n")
        fp.write("Total time per cycle: %s" % str(item[3]) + "\n")
        fp.write("Cooling time per cycle: %s" % str(item[4]) + "\n")
        fp.write("Heating time per cycle: %s" % str(item[5]) + "\n\n")
        
import csv

data= final

with open('final.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['cycle', 'local_min', 'local_max', 'total_time', 'cooling_time', 'heating_time'])
    for row in data:
        csv_out.writerow(row)  
 
# put data into a .csv (table)
        

    
#with open("final.txt", "w") as fp:
#    for item in totals[:47]:
#        fp.write("Cycle: %s" % item[0] + "\n")
#        fp.write("Starting force: %s" % item[1] + "\n")
#        fp.write("Ending force: %s" % item[2] + "\n\n")
#        fp.write("Cooling time: %s" % j + "\n")
#        fp.write("Heating time: %s" % i + "\n")
        

# 47 runs, and predict 3 cycles based on past data [48, 49. 50]
# Naive Bayes - can it give us a prediction of one point at a time,
# or a number of points?
        
# I'm not sure if we need extra point to predict data
# Predict next point based on first predicted point
# ----------------------------------------------------
# Use black to predict three points
        
# try and predict force and time for each point

# ignore min max, and let it predict the next point...let's see.

        
            