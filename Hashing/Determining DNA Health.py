#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())  # Number of genes
    genes = input().rstrip().split()  # List of gene strings
    health = list(map(int, input().rstrip().split()))  # List of health values corresponding to each gene
    s = int(input().strip())  # Number of DNA strands to process

    # Create a dictionary for gene -> health value
    gene_health = {genes[i]: health[i] for i in range(n)}

    # Variables to track the minimum and maximum health values
    min_health = float('inf')
    max_health = float('-inf')

    # Process each DNA strand
    for _ in range(s):
        # Read the start, end, and DNA string for this strand
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])  # Not used, but part of the input format
        last = int(first_multiple_input[1])  # Not used, but part of the input format
        dna = first_multiple_input[2]  # The DNA strand

        # Calculate the total health of this DNA strand
        total_health = 0
        
        # For each gene, check if it's present in the DNA strand
        for i in range(n):
            gene = genes[i]
            if gene in dna:
                total_health += gene_health[gene]

        # Track the minimum and maximum health
        min_health = min(min_health, total_health)
        max_health = max(max_health, total_health)

    # Print the result: minimum and maximum health
    print(min_health, max_health)
