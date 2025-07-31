#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n = len(container)
    
    # Calculate total balls in each container
    container_capacity = [sum(row) for row in container]
    
    # Calculate total balls of each type
    ball_type_count = [sum(container[i][j] for i in range(n)) for j in range(n)]
    
    # If sorted capacities and sorted ball counts match, it's possible
    return "Possible" if sorted(container_capacity) == sorted(ball_type_count) else "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
