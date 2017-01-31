#!/bin/python3
#Jumping on the Clouds: Revisited
import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
e = 100 - (n/k)
for i in range(0,n,k):
    if c[i] == 1:
        e -= 2
print(int(e))