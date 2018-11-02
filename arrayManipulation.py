#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    arr = [0 for _ in range(n)]
    for row in queries:
        x,y,inc = row
        arr[x-1] += inc
        try:
            arr[y] -= inc
        except:
            pass
    max = x = 0
    for num in arr:
        x += num 
        if max<x:
            max = x
    return max
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()