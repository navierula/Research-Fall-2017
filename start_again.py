#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:06:12 2017

@author: navrajnarula
"""

c = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112,
             108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]

min = []
max = []
for i, (first,second) in enumerate(zip(c, c[1:])):
    if first < second:
        min.append((i,first))
        continue
    if first > second:
        max.append((i,first))
        continue
        

#for i, (first,second) in enumerate(zip(c, c[1:])):
#    if i==0:
#        print("Start:", i, first)
#    elif i==len(c)-2:
#        print("End:", i+1, second)
#    elif first > second:
#        print("End:", i, first)
#        print("Start:", i+1, second)
