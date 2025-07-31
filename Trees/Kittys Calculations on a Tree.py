# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
from collections import defaultdict , deque

MOD = 10**9 + 7

def build_tree(n,edges):
    tree = defaultdict(list)
    for a,b in edges:
        tree[a].append(b)
        tree[b].append(a)
    return tree
    
def bfs_distance(tree,start):
    distances = {}
    queue = deque([start])
    distances[start] = 0
        
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            distances[neighbor] = distances[node] +1
            queue.append(neighbor)
    return distances
        
def calculate_expression(nodes, distances):
    total = 0
    k = len(nodes)
    for i in range(k):
        for j in range(i+1, k):
            u = nodes[i]
            v = nodes[j]
            dist = distances[u][v]
            total += (u * v * dist) % MOD
            total %= MOD
    return total
        
def kitty_calculations(n,edges,queries):
    tree = build_tree(n,edges)
    distances = {}
    for node in range(1, n + 1):
        distances[node] = bfs_distance(tree,node)
            
    results = []
    for k , nodes in queries:
        result = calculate_expression(node,distances)
        result.append(result)
    return results
        
if __name__ =='__main__':
    first_multiple_input = input().rstrip().split()
    n=int(first_multiple_input[0])
    q = int(first_multiple_input[1])
        
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int,input().rstrip.split())))
        
    queries =[]
    for _ in range(q):
        k = int(input().rstrip())
        nodes = list(map(int,input().rstrip().split()))

        queries.append((k,nodes))
    results = kitty_calculations(n,edges,queries)
        
    for result in results:
        print(result)
    
                        
            
            
