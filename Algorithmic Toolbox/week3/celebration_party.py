# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:45:46 2023

@author: Hzy
"""

def celebration_party_group(children):
    index = point = 0
    group = []
    cur_group = [children[0]]
    while index < (len(children)-1):
        if children[index+1] <= (children[point]+2):
            cur_group.append(children[index+1])
            index += 1
        else:
            index += 1            
            point = index
            group.append(cur_group)
            cur_group = [children[point]]
        
    group.append(cur_group)

    return(group)

if __name__ == '__main__':
    children = list(map(int,input().split()))
    print(celebration_party_group(children))