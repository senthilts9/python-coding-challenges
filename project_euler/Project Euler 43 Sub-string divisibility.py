# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import permutations

def has_substring_divisibility(pandigital):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if int(pandigital[i+1:i+4]) % primes[i] != 0:
            return False
    return True

def find_pandigital_sum(n):
    digits = ''.join(str(i) for i in range(n+1))
    total_sum = 0
    
    for perm in permutations(digits):
        num_str = ''.join(perm)
        if has_substring_divisibility(num_str):
            total_sum += int(num_str)
    
    print(total_sum)

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.read().strip())
    find_pandigital_sum(n)
