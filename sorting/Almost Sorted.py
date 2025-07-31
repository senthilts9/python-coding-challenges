#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Step 1: Check if already sorted
    if arr == sorted_arr:
        print("yes")
        return

    # Step 2: Find the first and last mismatched index
    l, r = 0, n - 1
    while arr[l] == sorted_arr[l]:  # Find first mismatch from the left
        l += 1
    while arr[r] == sorted_arr[r]:  # Find first mismatch from the right
        r -= 1

    # Step 3: Try swapping arr[l] and arr[r]
    arr[l], arr[r] = arr[r], arr[l]
    if arr == sorted_arr:
        print("yes")
        print(f"swap {l+1} {r+1}")  # Convert to 1-based index
        return
    arr[l], arr[r] = arr[r], arr[l]  # Undo swap

    # Step 4: Try reversing arr[l:r+1]
    arr[l:r+1] = arr[l:r+1][::-1]
    if arr == sorted_arr:
        print("yes")
        print(f"reverse {l+1} {r+1}")  # Convert to 1-based index
        return

    # Step 5: If neither swap nor reverse worked, print "no"
    print("no")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
