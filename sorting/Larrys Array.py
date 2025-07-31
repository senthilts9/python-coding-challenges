#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def count_inversions(A):
    """Count the number of inversions in the array."""
    inversions = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:  # Inversion found
                inversions += 1
    return inversions

def larrysArray(A):
    """Determine if the array can be sorted using 3-element rotations."""
    inversions = count_inversions(A)
    return "YES" if inversions % 2 == 0 else "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
