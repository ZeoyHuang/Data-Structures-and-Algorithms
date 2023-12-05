# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:49:24 2023

@author: Hzy
"""

def last_digit_of_Fib_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = [0,1]
        sum = 1
        for i in range(n-1):
            cur = (prev[0] + prev[1])%10
            prev[0] = prev[1]
            prev[1] = cur
            sum = sum + cur
        return (sum%10)

if __name__ == '__main__':
    n = int(input())
    print(last_digit_of_Fib_sum(n))