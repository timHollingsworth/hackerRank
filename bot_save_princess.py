#!/usr/bin/python
"""
    First time doing any machine learning in python. It's a little bit messy but i'm working on it.
    Works 100%
"""
def displayPathtoPrincess(n,grid):
    D = dict()
    count=0
    cnt=0
    for i in grid:
        cnt += 1
        arr = list(i)
        for a in arr:
            count += 1
            if a == 'p':
                D['princess'] = [cnt,count]
            if a == 'm':
                D['ME'] = [cnt,count]
        count=0
    if D['ME'][0] > D['princess'][0]:
        up,down = D['ME'][0] - D['princess'][0],0
    elif D['ME'][0] == D['princess'][0]:
        down,up = 0,0
    elif D['ME'][0] < D['princess'][0]:
        up,down = 0,D['princess'][0] - D['ME'][0]
    if D['ME'][1] > D['princess'][1]:
        left,right = D['ME'][1]-D['princess'][1],0
    elif D['ME'][1] == D['princess'][1]:
        left,right = 0,0
    elif D['ME'][1] < D['princess'][1]:
        left,right = 0,D['princess'][1]-D['ME'][1]
    if up > 0:
        for i in range(0,up):
            print("UP")
    if down > 0:
        for i in range(0,down):
            print("DOWN")
    if left > 0:
        for i in range(0,left):
            print("LEFT")
    if right > 0:
        for i in range(0,right):
            print("RIGHT")
    #print(up,down,left,right)
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)