# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:09:21 2023

@author: Hzy
"""

def max_salary(seq):
    # Custom sorting: sort based on which concatenation forms a bigger number
    seq.sort(key=lambda x: x*10, reverse=True)
    return ''.join(seq)

if __name__ == '__main__':
    n = int(input())
    seq = list(map(str, input().split()))
    print(max_salary(seq))