# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:54:39 2023

@author: Hzy
"""

import random

def quickSort(arr, left, right):
    if left < right:
        lt, gt = partition(arr, left, right)
        quickSort(arr, left, lt - 1)
        quickSort(arr, gt + 1, right)
    return arr

def partition(arr, left, right):
    pivot_index = random.randint(left, right)  # Randomly choose pivot
    pivot = arr[pivot_index]
    arr[pivot_index], arr[left] = arr[left], arr[pivot_index]  # Swap pivot with first element

    lt = left  # Less than pivot
    gt = right  # Greater than pivot
    i = left

    while i <= gt:
        if arr[i] < pivot:
            swap(arr, lt, i)
            lt += 1
            i += 1
        elif arr[i] > pivot:
            swap(arr, i, gt)
            gt -= 1
        else:
            i += 1

    return lt, gt

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    len_K = int(input())
    K = list(map(int, input().split()))
    quickSort(K, 0, len_K - 1)
    for i in K:
        print(i, end=' ')
