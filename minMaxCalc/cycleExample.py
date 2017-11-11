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
    
#############################

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
print(final_times)

########################################

lst = data_with_time

low_lst = []
high_lst = []

STATE = None
state_dict = {'low': low_lst, 'high': high_lst}

for x, y, z in lst:
    if z=='low' or z=='high':
        STATE = z
        sublist = []
        state_dict[STATE].append(sublist)
        sublist.append(x)
    if STATE and z=='NA':
        sublist.append(x)


    
#[(1, 'x', 'NA'),
# (2, 'x', 'low'),
# (3, 'x', 'NA'),
# (4, 'x', 'NA'),
# (5, 'x', 'NA'),
# (6, 'x', 'high'),
# (7, 'x', 'NA'),
# (8, 'x', 'NA'),
# (9, 'x', 'NA'),
# (10, 'x', 'NA'),
# (11, 'x', 'low'),
# (12, 'x', 'NA'),
# (13, 'x', 'NA'),
# (14, 'x', 'NA'),
# (15, 'x', 'high'),
# (16, 'x', 'NA'),
# (17, 'x', 'NA'),
# (18, 'x', 'NA'),
# (19, 'x', 'NA'),
# (20, 'x', 'NA'),
# (21, 'x', 'low'),
# (22, 'x', 'NA'),
# (23, 'x', 'NA'),
# (24, 'x', 'NA'),
# (25, 'x', 'high'),
# (26, 'x', 'NA')]    
#
#min_lst = [[2,3,4,5],[11,12,13,14], [21,22,23,24]]
#max_lst = [[6,7,8,9,10],[15,16,17,18,19,20], [25,26]]

    
    
#def partition_items(items):
#    lists = {
#        'min': [],
#        'max': [],
#    }
#    vals_list_max = []
#    vals_list_min = []
#    current_kind = None
#    current_list = None
#    for value, _, kind in items:
#        if kind != current_kind and kind != 'NA':
#            vals_list_max.append(value)
#           # print(vals_list_max)
#           # print(kind)
#            current_kind = kind
#           # print(current_kind)
#            # You'll get a error here if current_kind isn't one of 'min'
#            # or 'max'.
#            current_list = lists[current_kind]
#            #print(current_list)
#            current_list.append(0)
#            #print(current_list)
#        # You'll get an error here if the first item in the list doesn't
#        # have type of 'min' or 'max'.
#        current_list[-1] += value
#        print(current_list)
# 
#    return lists
#
#
#lists = partition_items(data_with_time)
#print(lists['min'])
## -> [15, 50, 115]
#print(lists['max'])

        
        
        
    
    
    
    
     