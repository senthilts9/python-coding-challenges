#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    H = len(A)
    W = len(A[0])
    total_surface_area = 0

    # Iterate over each cell in the grid
    for i in range(H):
        for j in range(W):
            height = A[i][j]
            
            # Top and bottom surfaces (always 1 each)
            total_surface_area += 2  

            # Check all four sides (left, right, front, back)
            # Left side
            if j == 0:
                total_surface_area += height  # Fully exposed edge
            else:
                total_surface_area += max(0, height - A[i][j - 1])  # Difference with left neighbor

            # Right side
            if j == W - 1:
                total_surface_area += height  # Fully exposed edge
            else:
                total_surface_area += max(0, height - A[i][j + 1])  # Difference with right neighbor

            # Front side
            if i == 0:
                total_surface_area += height  # Fully exposed edge
            else:
                total_surface_area += max(0, height - A[i - 1][j])  # Difference with front neighbor

            # Back side
            if i == H - 1:
                total_surface_area += height  # Fully exposed edge
            else:
                total_surface_area += max(0, height - A[i + 1][j])  # Difference with back neighbor
    
    return total_surface_area

    #print(total_surface_area)  # Print final surface area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
