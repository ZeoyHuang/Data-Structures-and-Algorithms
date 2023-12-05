# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:27:54 2023

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

def bin_search_list(K,Q):
    Q_in_K = []
    for i in Q:
        Q_in_K.append(bin_search(K,i))
    return Q_in_K

if __name__ == '__main__':
    len_K = int(input())
    K = list(map(int,input().split()))
    len_Q = int(input())
    Q = list(map(int,input().split()))
    for i in bin_search_list(K,Q):
        print(i,end=' ')