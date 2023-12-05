# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:45:37 2023

@author: Hzy
"""

def money_change(total):
    change = 0
    coins = [10,5,1]
    for i in range(len(coins)):
        if total/coins[i] > 0:
            change += int(total/coins[i])
            total = total %  coins[i]
    return change

if __name__ == '__main__':
    total = int(input())
    print(money_change(total))