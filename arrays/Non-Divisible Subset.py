#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    remainder_count = [0] * k
    
    # Count the number of elements for each remainder when divided by k
    for num in s:
        remainder_count[num % k] += 1

    # Step 2: Handle the special case for remainder 0
    subset_size = min(remainder_count[0], 1)

    # Step 3: For each remainder pair, select the maximum count of either remainder
    for i in range(1, (k // 2) + 1):
        if i != k - i:  # If the remainders are not the same (e.g., 1 and k-1)
            subset_size += max(remainder_count[i], remainder_count[k - i])
        else:  # If remainders are the same (e.g., k/2 when k is even)
            subset_size += min(remainder_count[i], 1)

    return subset_size
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
