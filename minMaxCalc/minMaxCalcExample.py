h#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An implementation of calculating local minima and maxima on a smaller example!
"""
import pandas as pd

# read in dataset
xl = pd.ExcelFile("data/130N_Cycles_1-47.xlsx")
df = xl.parse("Specimen_RawData_1")
df

# append data from load column to list
load = []
for item in df.index:
    load.append(df["Round"][item])
    
trial_lst = load


#trial_lst = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             #108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]
             
trial_lst = [0.5, 3, 6, 58, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]

trial_lst = load


indices = [x[0] for x in enumerate(map(lambda x:x<1, trial_lst)) if x[1]]


sublists = [trial_lst[i:j] for i,j in list(zip([0]+indices, indices+[None]))[1:]]


for i,l in enumerate(sublists):
    print(i, max((v,i) for (i,v) in enumerate(l)), min((v,i) for (i,v) in enumerate(l)))
    
