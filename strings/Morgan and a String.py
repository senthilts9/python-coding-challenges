#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Write your code here
    i, j = 0, 0
    result = []
    
    # Iterate until both strings are exhausted
    while i < len(a) and j < len(b):
        # If the characters at the top of both stacks are different
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            # If the characters are the same, look ahead to decide
            if a[i:] < b[j:]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
    
    # Append the remaining characters from a or b
    result.append(a[i:])
    result.append(b[j:])
    
    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
