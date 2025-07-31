# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

K,M = map(int, input().strip().split())
lists = []

for _ in range(K):
    data = list(map(int,input().strip().split()))
    Ni = data[0]
    elements = data[1:Ni + 1 ]
    lists.append(elements)
    
max_S =0 

for combination in product(*lists):
    current_sum = sum(x**2 for x in combination) % M
    max_S = max(max_S,current_sum)
    

print(max_S)



    
