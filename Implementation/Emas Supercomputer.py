#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#


def get_max_plus_size(grid, r, c):
    """Compute the maximum possible arm length for a plus centered at (r, c)."""
    max_size = 0
    while (r - max_size >= 0 and r + max_size < len(grid) and
           c - max_size >= 0 and c + max_size < len(grid[0]) and
           grid[r - max_size][c] == 'G' and grid[r + max_size][c] == 'G' and
           grid[r][c - max_size] == 'G' and grid[r][c + max_size] == 'G'):
        max_size += 1
    return max_size - 1  # Adjust because we go one step too far in the loop

def get_all_pluses(grid):
    """Find all valid pluses and store them with their areas."""
    pluses = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'G':
                max_size = get_max_plus_size(grid, r, c)
                for size in range(max_size + 1):
                    area = 4 * size + 1
                    pluses.append((area, r, c, size))
    return sorted(pluses, reverse=True)  # Sort by descending area

def does_overlap(p1, p2):
    """Check if two pluses overlap in the grid."""
    _, r1, c1, size1 = p1
    _, r2, c2, size2 = p2
    
    # Get all cells occupied by the first plus
    cells1 = {(r1, c1)}
    for i in range(1, size1 + 1):
        cells1.update({(r1 + i, c1), (r1 - i, c1), (r1, c1 + i), (r1, c1 - i)})
    
    # Check if any cell from plus2 is in plus1
    if (r2, c2) in cells1:
        return True
    for i in range(1, size2 + 1):
        if {(r2 + i, c2), (r2 - i, c2), (r2, c2 + i), (r2, c2 - i)} & cells1:
            return True
    
    return False

def twoPluses(grid):
    pluses = get_all_pluses(grid)
    max_product = 0
    
    # Iterate through all pairs of pluses
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            if not does_overlap(pluses[i], pluses[j]):
                max_product = max(max_product, pluses[i][0] * pluses[j][0])
                break  # No need to check smaller pluses

    return max_product
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
