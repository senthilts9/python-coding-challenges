#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    chars = list(w)
    n = len(chars)
    
    # Step 1: Find the rightmost character which is smaller than its next character
    i = n - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1
    
    # If no such character is found, that means we are at the last permutation
    if i == -1:
        return "no answer"
    
    # Step 2: Find the rightmost character that is greater than chars[i]
    j = n - 1
    while chars[j] <= chars[i]:
        j -= 1
    
    # Step 3: Swap characters at i and j
    chars[i], chars[j] = chars[j], chars[i]
    
    # Step 4: Reverse the sequence from i + 1 to the end of the list
    chars = chars[:i + 1] + chars[i + 1:][::-1]
    
    # Convert the list back to a string
    return ''.join(chars)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
