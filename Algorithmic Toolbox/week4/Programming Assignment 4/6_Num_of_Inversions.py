# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:07:31 2023

@author: Hzy
"""

def merge_and_count(arr, left, mid, right):
    # Create temporary arrays for left and right halves
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    # Initialize indices for left, right, and merged arrays
    i = 0
    j = 0
    k = left
    inv_count = 0

    # Merge the two halves and count inversions
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inv_count += len(left_half) - i  # Corrected the count here
        k += 1

    # Copy the remaining elements (if any)
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return inv_count

def merge_sort_and_count(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2

        # Count inversions in left and right halves
        count += merge_sort_and_count(arr, left, mid)
        count += merge_sort_and_count(arr, mid + 1, right)

        # Count cross inversions and merge
        count += merge_and_count(arr, left, mid, right)

    return count

if __name__ == '__main__':
    len_K = int(input())
    K = list(map(int,input().split()))
    print(merge_sort_and_count(K, 0, len_K - 1))

