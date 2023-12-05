# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:05:34 2023

@author: Hzy
"""

def max_product(n,clicks,prices):
    clicks.sort()
    prices.sort()
    product = 0
    for i in range(len(clicks)):
        product += clicks[i] * prices[i]
    return product

if __name__ == '__main__':
    n = int(input())
    clicks = list(map(int,input().split()))
    prices = list(map(int,input().split()))
    print(max_product(n,clicks,prices))
