# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:54:40 2023

@author: Hzy
"""

import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    num_points = len(points_sorted_by_x)
    if num_points <= 3:
        return min([euclidean_distance(points_sorted_by_x[i], points_sorted_by_x[j]) 
                    for i in range(num_points) for j in range(i+1, num_points)])

    mid = num_points // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    # Divide points in Y sorted array into two halves
    midpoint = points_sorted_by_x[mid][0]
    left_half_y = list(filter(lambda x: x[0] <= midpoint, points_sorted_by_y))
    right_half_y = list(filter(lambda x: x[0] > midpoint, points_sorted_by_y))

    # Recursive calls
    min_distance_left = closest_pair_recursive(left_half, left_half_y)
    min_distance_right = closest_pair_recursive(right_half, right_half_y)
    min_distance = min(min_distance_left, min_distance_right)

    # Combine step
    strip = [p for p in points_sorted_by_y if abs(p[0] - midpoint) < min_distance]
    for i in range(len(strip)):
        for j in range(i+1, min(i + 7, len(strip))):
            min_distance = min(min_distance, euclidean_distance(strip[i], strip[j]))

    return min_distance

def closest_pair_of_points(points):
    points_sorted_by_x = sorted(points, key=lambda x: (x[0], x[1]))
    points_sorted_by_y = sorted(points, key=lambda x: (x[1], x[0]))
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

if __name__ == '__main__':
    num_points = int(input())
    points = []
    for _ in range(num_points):
        x, y = map(int, input().split())
        points.append((x, y))

    min_distance = closest_pair_of_points(points)
    print(min_distance)