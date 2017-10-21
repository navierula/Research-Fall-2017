#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bringing all parts of the code together in a small example
"""

trial_lst = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]

trial_lst.sort(key=float)

totals = []
for count, items in enumerate(trial_lst):

    counter = count + 1
    last_object = (trial_lst[count], trial_lst[(len(trial_lst)-1) - count])
    totals.append(last_object)

totals = totals[:3]

data_ = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]

combine_data = []
for i in range(len(data_)):
    flag = 0
    for j in totals:
        if data_[i] == j[0]:
            combine_data.append((data_[i], "min"))
            flag = 1
        if data_[i] == j[1]:
            combine_data.append((data_[i], "max"))
            flag = 1
    if flag == 0:
        combine_data.append((data_[i],"NA")) 
           
data_two = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]

count = 0
data_with_time = []
for item in combine_data:
    count += 1
    data_with_time.append((count,) +item)


min_sums = []
max_sums = []
for x, _, what in data_with_time:
    if what != 'NA':
        current = min_sums if what == 'min' else max_sums
        current.append(0)
    current[-1] += x

    
    
    

        
        
        
    
    
    
    
     