# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import comb

N = int(input().strip())
letters = input().strip().split()
K = int(input().strip())

count_a = letters.count('a')

total_combinations = comb(N,K)


if count_a ==0 :
    probability =0.0
else:
    not_a_combination = comb(N - count_a,K) if N - count_a >= K else 0 
    probability = 1 - (not_a_combination/ total_combinations)
    
   

print(f"{probability:.4f}")
