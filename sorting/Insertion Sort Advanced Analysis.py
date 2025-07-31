#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    # Write your code here
    total_shifts = 0  # To track the number of shifts
    n = len(arr)
    
    # We start from the second element because the first element is already considered sorted
    for i in range(1, n):
        # Store the current element to be inserted
        current_value = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than current_value, to one position ahead
        j = i - 1
        shifts = 0
        
        # Count the shifts as long as elements are greater than the current_value
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1
            shifts += 1
        
        # Insert the current_value into its correct position
        arr[j + 1] = current_value
        
        # Add the shifts made for this iteration to the total
        total_shifts += shifts
    
    return total_shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
