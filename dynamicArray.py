#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastAnswer = 0
    result = []
    seq = [[] for _ in range(n)]
    for row in queries:
        index = (row[1] ^ lastAnswer) % n
        if row[0] == 1:
            seq[index].append(row[2])
        elif row[0] == 2:
            size = len(seq[index])
            lastAnswer = seq[index][row[2] % size]
            result.append(lastAnswer)
            print(lastAnswer)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()