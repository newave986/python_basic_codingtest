# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:54:57 2021

@author: newave986.git
"""

import sys as sys
from collections import deque

num = int(sys.stdin.readline())

for k in range(num):
    
    ver, edg = map(int, sys.stdin.readline().split())
    my_list = [[] for _ in range(ver+1)]
    queue = deque()
    
    for i in range(edg):
        a, b = map(int, sys.stdin.readline().split())
        my_list[a].append(b)
        my_list[b].append(a)
    
    level = [0 for _ in range(ver + 1)]
    status = True
    
    queue.append(1)
    level[1] = 1
    
    while queue:
        
        k = queue.popleft()
    
        for t in my_list[k]:
                    
            if level[t] == 0:
                level[t] = -level[k]
                queue.append(t)
                    
            elif level[t] == level[k]:
                 status = False
                 break
    
    del level[0]
    if 0 in level:
        status = False
    
    if status == False: print("NO")
    else: print("YES")
