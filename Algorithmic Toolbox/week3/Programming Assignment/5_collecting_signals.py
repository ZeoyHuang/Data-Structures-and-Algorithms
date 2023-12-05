# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:15:22 2023

@author: Hzy
"""

def collect_sign(n,signals):
    signals.sort(key=lambda x: x[0])
    
    collect = []
    last_covered_point = -1

    for left, right in signals:
        # If the current segment starts after the last covered point, select a new point
        if left > last_covered_point:
            last_covered_point = right
            collect.append(last_covered_point)

    return collect
        
if __name__ == '__main__':
    n = int(input())
    signals = []
    for i in range(n):
        signals.append(list(map(int,input().split())))
    
    print(len(collect_sign(n,signals)))
    for i in range(len(collect_sign(n,signals))):
        print(collect_sign(n,signals)[i],end=' ')