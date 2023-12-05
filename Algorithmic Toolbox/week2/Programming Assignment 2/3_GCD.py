# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:13:57 2023

@author: Hzy
"""

def get_GCD(a,b):
    if a>b:
        temp = a
        a = b
        b = temp
    
    while a != 0:
        temp = a
        a = b % a
        b = temp
        
    return b

if __name__ == '__main__':
    input_num = list(map(int,input().split()))
    a = input_num[1]
    b = input_num[0]
    print(get_GCD(a,b))