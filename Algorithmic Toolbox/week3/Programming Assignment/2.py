# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:54:56 2023

@author: Hzy
"""

def maximize_loot(n, W, items):
    # Calculate value-to-weight ratio and store with weight and value
    items = sorted([(value / weight, weight, value) for value, weight in items], reverse=True)
    
    total_value = 0
    for ratio, weight, value in items:
        if W == 0:
            return total_value

        # Calculate the amount of weight to take from the current item
        amount = min(weight, W)
        total_value += amount * ratio
        W -= amount

    return total_value

# Main execution
if __name__ == '__main__':
    n, W = map(int, input().split())
    items = []
    for _ in range(n):
        c, w = map(int, input().split())
        items.append((c, w))

    max_value = maximize_loot(n, W, items)
    print(f"{max_value:.4f}")

        