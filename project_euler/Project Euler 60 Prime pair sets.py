import sys
import math
import time

# Global cache for concatenation check results.
concat_cache = {}

# Cache for string representations of primes.
prime_str = {}

def is_prime(n):
    if n < 2:
        return False
    # Check small primes
    for p in (2, 3, 5, 7, 11):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Use bases sufficient for n < 3.5e12.
    for a in (2, 3, 5, 7, 11):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def sieve(limit):
    mark = [True]*(limit+1)
    mark[0] = mark[1] = False
    p = 2
    while p * p <= limit:
        if mark[p]:
            for i in range(p*p, limit+1, p):
                mark[i] = False
        p += 1
    return [i for i in range(2, limit+1) if mark[i]]

def concat_check(p, q):
    # Always called with p < q.
    key = (p, q)
    if key in concat_cache:
        return concat_cache[key]
    s1 = prime_str[p] + prime_str[q]
    s2 = prime_str[q] + prime_str[p]
    num1 = int(s1)
    num2 = int(s2)
    res = is_prime(num1) and is_prime(num2)
    concat_cache[key] = res
    return res

def build_compat(primes):
    # Build a dictionary mapping each prime to the set of primes (greater than it)
    # with which it is mutually compatible.
    compat = {}
    L = len(primes)
    for i in range(L):
        p = primes[i]
        compat[p] = set()
        for j in range(i+1, L):
            q = primes[j]
            if concat_check(p, q):
                compat[p].add(q)
    return compat

def dfs(clique, K, compat, results):
    if len(clique) == K:
        results.append(sum(clique))
        return
    # If clique is empty, iterate over all primes in sorted order.
    if not clique:
        for p in sorted(compat.keys()):
            dfs([p], K, compat, results)
    else:
        # Intersection of compatibility sets for all primes in the current clique.
        cand = None
        for p in clique:
            if cand is None:
                cand = set(compat[p])
            else:
                cand = cand.intersection(compat[p])
        if cand is None:
            return
        # Ensure candidates are greater than the last element (to maintain order).
        last = clique[-1]
        for q in sorted(x for x in cand if x > last):
            dfs(clique + [q], K, compat, results)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    try:
        N = int(data[0])
        K = int(data[1])
    except:
        sys.exit("Invalid input format")
    # Generate primes less than N.
    all_primes = sieve(N-1)
    # Build a dictionary of string representations for each prime.
    for p in all_primes:
        prime_str[p] = str(p)
    # Build compatibility graph only for primes < N.
    compat = build_compat(all_primes)
    results = []
    dfs([], K, compat, results)
    # Remove duplicates, sort and print one per line.
    out = sorted(set(results))
    sys.stdout.write("\n".join(str(x) for x in out))

#######################
# Testing Harness
#######################
def run_tests():
    import io
    def run_io_fun(input_data, func):
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        try:
            func()
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    # Positive Test:
    # Sample Input: "700 3"
    # Expected Output (each valid set's sum, sorted): "107" and "123" on separate lines.
    input_data = "700 3"
    expected_lines = ["107", "123"]
    output = run_io_fun(input_data, solve)
    out_lines = output.splitlines()
    assert sorted(out_lines) == sorted(expected_lines), "Positive test failed. Expected: " + str(expected_lines) + " Got: " + str(out_lines)
    print("Positive test passed.")

    # Negative Test:
    # For a small N with no set of 3 primes having this property.
    input_data = "200 3"
    output = run_io_fun(input_data, solve)
    # In this case, output should be empty.
    assert output.strip() == "", "Negative test failed. Expected empty output. Got: " + output
    print("Negative test passed.")

    # Additional Test (Multiple Cases):
    # For instance, try K=3 with N=1000.
    input_data = "1000 3"
    output = run_io_fun(input_data, solve)
    # We do not assert exact result here but print the result.
    print("Additional test (1000 3) output:")
    print(output)

    # Performance Test:
    # Worst-case: N=20000, K=3 (or K=4/5). Measure elapsed time.
    input_data = "20000 3"
    start = time.time()
    _ = run_io_fun(input_data, solve)
    end = time.time()
    print("Performance test for N=20000, K=3 completed in %.3f seconds." % (end - start))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        solve()
