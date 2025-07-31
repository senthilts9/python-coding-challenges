#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    n = len(arr)
    count = 1
    
    
    for j in range(n):
        max_value = arr[j]
     
        for i in range(j):
            max_value = max(max_value, arr[i])
            if arr[i] * arr[j] <= max_value:
                count += 1
    return count
        
       
            
  
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
