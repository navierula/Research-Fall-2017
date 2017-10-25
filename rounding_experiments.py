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

# append data from round zero column to list
round_zero = []
for item in df.index:
    round_zero.append(df["Round_Zero"][item])
    
# append data from round one column to list
round_one = []
for item in df.index:
    round_one.append(df["Round_One"][item])
    
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

count = 0
new = []
for t in get_groups(round_zero):
    new.append(t)
    if count <= 5:
        print(t)
        count += 1
    
gen = get_groups(round_zero)


for i, (t1, t2) in enumerate(zip(gen, gen), 1):
    print(i, t1[0], t2)