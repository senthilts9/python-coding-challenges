#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar_list = []
    
    for num in range(p, q + 1):
        square = str(num ** 2)  # Square the number and convert to string
        d = len(str(num))  # Number of digits in the original number
        
        # Split the square into two parts
        right = square[-d:]  # Last 'd' digits
        left = square[:-d] if square[:-d] else '0'  # Remaining left part, default to '0'
        
        # Convert to integers and check Kaprekar condition
        if int(left) + int(right) == num:
            kaprekar_list.append(str(num))

    # Print result
    print(" ".join(kaprekar_list) if kaprekar_list else "INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
