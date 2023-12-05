# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:48:22 2023

@author: Hzy
"""

def major_elem(K):
    dic = {}
    for i in K:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for m in dic:
        if dic[m] > len(K)/2:
            return 1
    return 0
    
if __name__ == '__main__':
    len_K = int(input())
    K = list(map(int,input().split()))
    print(major_elem(K))