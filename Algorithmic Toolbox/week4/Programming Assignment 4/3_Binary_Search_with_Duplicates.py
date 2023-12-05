# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:47:56 2023

@author: Hzy
"""

def bin_search(K, q):
    left = 0
    right = len(K) - 1
    result = -1  # Use this to store the index when found

    while left <= right:
        middle = left + (right - left) // 2  # To prevent overflow

        if K[middle] > q:
            right = middle - 1
        elif K[middle] < q:
            left = middle + 1
        else:
            result = middle  # Store the index
            right = middle - 1  # Continue searching in the left half

    return result


def find_dup(K,q):
    flag = bin_search(K,q)
    if flag == -1:
        return -1
    elif flag == 0:
        return 0
    else:
        while K[flag] == q:
            flag -= 1
        return flag+1


def bin_search_list(K,Q):
    Q_in_K = []
    for i in Q:
        Q_in_K.append(find_dup(K,i))
    return Q_in_K

if __name__ == '__main__':
    len_K = int(input())
    K = list(map(int,input().split()))
    len_Q = int(input())
    Q = list(map(int,input().split()))
    for i in bin_search_list(K,Q):
        print(i,end=' ')