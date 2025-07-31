#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd
from functools import reduce
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


    
def lcm(a, b):
    return (a * b) // gcd(a, b)

def getTotalX(a, b):
    # Find LCM of array 'a'
    lcm_a = reduce(lcm, a)

    # Find GCD of array 'b'
    gcd_b = reduce(gcd, b)

    # Count numbers that are multiples of lcm_a and divisors of gcd_b
    count = 0
    for x in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % x == 0:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
