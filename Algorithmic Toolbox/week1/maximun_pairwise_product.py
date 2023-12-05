# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:11:53 2023

@author: Hzy
"""

n = int(input())
seq = input().split()

max1 = max2 = 0
for item in seq:
    if int(item)>max1:
        max1 = int(item)
seq.remove(str(max1))
for item in seq:
    if int(item)>max2:
        max2 = int(item)

print(max1 * max2)