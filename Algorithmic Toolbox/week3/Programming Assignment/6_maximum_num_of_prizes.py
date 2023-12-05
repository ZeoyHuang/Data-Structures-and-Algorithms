# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:49:52 2023

@author: Hzy
"""


def max_k(n):
    k = 0
    while (k * (k + 1)) // 2 <= n:
        k += 1
    return k - 1  # Subtract 1 because the loop exits when the sum exceeds n

def summands(n):
    k = max_k(n)
    outcome = list(range(1, k + 1))
    outcome[-1] += n - sum(outcome)
    return outcome

if __name__ == '__main__':
    n = int(input())
    result = summands(n)
    print(len(result))
    for item in result:
        print(item, end=' ')