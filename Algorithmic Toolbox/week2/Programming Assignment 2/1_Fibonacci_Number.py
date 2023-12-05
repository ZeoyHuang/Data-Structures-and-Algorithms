# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:54:42 2023

@author: Hzy
"""

def get_fib_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = [0,1]
        for i in range(n-1):
            cur = prev[0] + prev[1]
            prev[0] = prev[1]
            prev[1] = cur
        return cur

if __name__ == '__main__':
    n = int(input())
    print(get_fib_number(n))