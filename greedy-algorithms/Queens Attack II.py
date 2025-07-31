#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obstacle_set = set(tuple(obstacle) for obstacle in obstacles)
    
    # Directions for the queen's movement: up, down, left, right, and the 4 diagonals
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    attackable_squares = 0
    
    # For each direction, we move step by step from the queen's position
    for direction in directions:
        # Direction is a tuple (row_change, col_change)
        row, col = r_q, c_q
        while True:
            # Move in the current direction
            row += direction[0]
            col += direction[1]
            
            # Check if the new position is out of bounds
            if not (1 <= row <= n and 1 <= col <= n):
                break
            
            # If there's an obstacle in the way, we stop
            if (row, col) in obstacle_set:
                break
            
            # Otherwise, this square can be attacked
            attackable_squares += 1
    
    return attackable_squares


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
