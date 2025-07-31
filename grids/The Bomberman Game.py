#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def detonate(grid, r, c):
    """Simulates the detonation process."""
    new_grid = [['O'] * c for _ in range(r)]  # Assume a full grid of bombs
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':  # Bomb is present
                new_grid[i][j] = '.'  # Detonate itself
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < r and 0 <= nj < c:
                        new_grid[ni][nj] = '.'  # Detonate neighbors
    
    return ["".join(row) for row in new_grid]

def bomberMan(n, grid):
    r, c = len(grid), len(grid[0])

    if n == 1:
        return grid  # No changes if n == 1
    
    if n % 2 == 0:
        return ["O" * c for _ in range(r)]  # Full bomb grid if n is even
    
    # Compute two bomb detonation cycles
    first_detonation = detonate(grid, r, c)
    second_detonation = detonate(first_detonation, r, c)
    
    return first_detonation if n % 4 == 3 else second_detonation


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
