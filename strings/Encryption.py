#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    
    # Step 2: Find the length of the string
    L = len(s)
    
    # Step 3: Calculate the number of rows and columns
    r = int(math.floor(math.sqrt(L)))  # Find the row count as the floor value of the square root
    c = int(math.ceil(L / r))  # Calculate columns needed based on the string length
    
    # Check if the calculated grid can fit the string length, if not, adjust rows
    while r * c < L:
        r += 1
        c = int(math.ceil(L / r))  # Recalculate columns if rows increase
    
    # Step 4: Fill the grid row by row
    grid = []
    for i in range(0, L, c):
        grid.append(s[i:i+c])  # Add substrings to grid

    # Step 5: Read the grid column by column and generate the encoded message
    encoded_message = []
    for col in range(c):
        column_str = ''.join(row[col] if col < len(row) else '' for row in grid)
        encoded_message.append(column_str)
    
    # Step 6: Join the columns with a space and return the result
    return ' '.join(encoded_message)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
