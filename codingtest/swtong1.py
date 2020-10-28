#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSum(arr):
    # Write your code here
    for i in range(len(arr)-1):
        if sum(arr[0:i] == arr[i+1:len(arr)-1]):
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = balancedSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
