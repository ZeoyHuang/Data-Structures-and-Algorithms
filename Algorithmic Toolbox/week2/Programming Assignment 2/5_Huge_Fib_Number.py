# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:45:03 2023

@author: Hzy
"""

def huge_fib_number(n,m):
    if n == 0:
        return (0%m)
    elif n == 1:
        return (1%m)
    else:
        prev = [0,0]
        prev[0] = 0%m
        prev[1] = 1%m
        for i in range(n-1):
            cur = (prev[0] + prev[1])%m
            prev[0] = prev[1]
            prev[1] = cur
        return cur

if __name__ == '__main__':
    input_num = list(map(int,input().split()))
    n = input_num[0]
    m = input_num[1]
    print(huge_fib_number(n,m))