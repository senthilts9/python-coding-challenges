#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    index_map = {}
    min_distance = float('inf')  # Initialize with a large number
    
    for i, num in enumerate(a):
        if num in index_map:
            min_distance = min(min_distance, i - index_map[num])
        index_map[num] = i  # Store the last seen index of the number

    return min_distance if min_distance != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
