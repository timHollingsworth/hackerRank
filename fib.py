#!/bin/python3

import sys

def fib(n):
    score = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    return fib(n-1) + fib(n-2)



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    tmp = []
    for i in range(3,n,3):
        f = fib(i)
        if i <= n:
            tmp.append(f)
    print(sum(tmp))