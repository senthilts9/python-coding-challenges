import sys
import math

# Check whether x is a perfect power (i.e. x = r^d for some integers r>=2, d>=2).
def is_perfect_power(x):
    # For x < 4, no representation with d>=2.
    if x < 4:
        return False
    # Try exponents from 2 up to floor(log2(x))+1.
    max_d = int(math.log(x, 2)) + 2
    for d in range(2, max_d):
        # Compute the d-th root of x (using floating point)
        r = int(round(x**(1.0/d)))
        # Due to rounding, check both r and r+1.
        if r > 1 and r**d == x:
            return True
        if (r+1)**d == x:
            return True
    return False

# For a given a and N, compute k = max { d >= 1 such that a^d <= N }.
def max_exponent(a, N):
    d = 1
    prod = a
    while prod * a <= N:
        prod *= a
        d += 1
    return d

# Precompute F[k] = number of distinct products in the set 
#       { d * b : d = 1..k, b = 2..N }.
def precompute_F(N, max_k):
    F = [0] * (max_k + 1)  # we will use indices 1..max_k
    for k in range(1, max_k + 1):
        size = k * N + 1  # maximum product is k*N
        mark = [False] * (size)
        # For each d from 1 to k, mark all products d*b for b in [2, N].
        for d in range(1, k + 1):
            # Instead of iterating with a Python loop over b, we loop from 2 to N.
            for b in range(2, N + 1):
                mark[d * b] = True
        F[k] = sum(mark)  # True counts as 1
    return F

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    try:
        N = int(data[0])
    except:
        sys.exit("Invalid input")
    
    # Determine the maximum possible k that can occur.
    # For any primitive a, k = max { d : a^d <= N }.
    # The worst-case (largest k) happens for a = 2.
    max_k_possible = 0
    prod = 1
    while True:
        prod *= 2
        if prod <= N:
            max_k_possible += 1
        else:
            break

    # Precompute F[k] for k = 1 to max_k_possible.
    F = precompute_F(N, max_k_possible)
    
    ans = 0
    # Loop over a from 2 to N.
    for a in range(2, N + 1):
        # Only count primitive numbers.
        if is_perfect_power(a):
            continue
        # Compute k = max exponent such that a^k <= N.
        k = max_exponent(a, N)
        # Add the count F[k] for this base.
        ans += F[k]
    
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()
