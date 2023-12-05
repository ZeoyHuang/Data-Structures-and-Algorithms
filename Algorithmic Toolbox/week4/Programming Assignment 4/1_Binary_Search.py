# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:17:40 2023

@author: Hzy
"""

def bin_search(K,q):
    left = 0
    right = len(K)-1
    middle = int((left+right)/2)
    while right != left:
        if K[middle] > q:
            right = middle
            middle = int((left+right)/2)
        elif K[middle] < q:
            left = middle
            middle = int((left+right)/2)
        else:
            return middle
        
        if right == middle or left == middle:
            if K[right] == q:
                return right
            elif K[left] == q:
                return left
            else:
                return -1
    return -1

if __name__ == '__main__':
    K = list(map(int,input().split()))
    q = int(input())
    print(bin_search(K,q))