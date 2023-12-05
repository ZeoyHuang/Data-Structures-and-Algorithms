# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:15:54 2023

@author: Hzy
"""

def car_fuel(d, m, n, stops):
    stops.append(d)  # Add destination to the list of stops
    current_position = 0
    count = 0
    last_stop = 0

    for stop in stops:
        # Check if the next stop is too far to reach
        if stop - last_stop > m:
            return -1

        # If we need to refuel before the next stop
        if stop > current_position + m:
            current_position = last_stop  # Refuel at the last stop
            count += 1

        last_stop = stop

    return count

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int,input().split()))
    print(car_fuel(d,m,n,stops))