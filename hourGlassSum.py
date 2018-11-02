#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_arr = []
    for row_index in range(len(arr)):
        for index in range(len(arr[row_index])):
            try:   
                if type(arr[row_index][index]) == int and type(arr[row_index][index+2]) == int and type(arr[row_index+1][index+1]) == int and type(arr[row_index+2][index+2]) == int:
                    temp_arr = [arr[row_index][index],arr[row_index][index+1],arr[row_index][index+2],arr[row_index+1][index+1],arr[row_index+2][index], arr[row_index+2][index+1], arr[row_index+2][index+2]]
                    sum_arr.append(sum(temp_arr))
            except:
                pass

    return max(sum_arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()