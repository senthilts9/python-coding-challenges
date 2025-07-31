#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    m = len(matrix)
    n = len(matrix[0])

    # Determine the number of layers
    layers = min(m, n) // 2
    
    # Helper function to extract a layer from the matrix
    def extract_layer(layer_num):
        layer = []
        # Top row
        for i in range(layer_num, n - layer_num):
            layer.append(matrix[layer_num][i])
        # Right column
        for i in range(layer_num + 1, m - layer_num - 1):
            layer.append(matrix[i][n - layer_num - 1])
        # Bottom row
        for i in range(n - layer_num - 1, layer_num - 1, -1):
            layer.append(matrix[m - layer_num - 1][i])
        # Left column
        for i in range(m - layer_num - 2, layer_num, -1):
            layer.append(matrix[i][layer_num])
        return layer
    
    # Helper function to insert a layer back into the matrix
    def insert_layer(layer_num, rotated_layer):
        idx = 0
        # Top row
        for i in range(layer_num, n - layer_num):
            matrix[layer_num][i] = rotated_layer[idx]
            idx += 1
        # Right column
        for i in range(layer_num + 1, m - layer_num - 1):
            matrix[i][n - layer_num - 1] = rotated_layer[idx]
            idx += 1
        # Bottom row
        for i in range(n - layer_num - 1, layer_num - 1, -1):
            matrix[m - layer_num - 1][i] = rotated_layer[idx]
            idx += 1
        # Left column
        for i in range(m - layer_num - 2, layer_num, -1):
            matrix[i][layer_num] = rotated_layer[idx]
            idx += 1
    
    # Process each layer
    for layer_num in range(layers):
        # Extract the layer
        layer = extract_layer(layer_num)
        # Rotate the layer
        rotated_layer = layer[r % len(layer):] + layer[:r % len(layer)]
        # Insert the rotated layer back into the matrix
        insert_layer(layer_num, rotated_layer)
    
    # Print the result matrix
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
