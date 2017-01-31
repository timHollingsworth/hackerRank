#!/bin/python3

import sys


n = int(input().strip())
a = []
d1 = []
d2 = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
count=0
n -= 1
for i in a:
    d1.append(i[count])
    d2.append(i[(n - count)])
    count += 1
sum = sum(d1) - sum(d2)
print(abs(sum))
