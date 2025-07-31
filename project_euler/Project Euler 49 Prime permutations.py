import sys
import math
import time

def sieve(n):
    # Sieve of Eratosthenes to return list of primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]

def find_sequences(N, K):
    # We are to find all sequences of K primes in arithmetic progression
    # such that all terms are permutations of each other.
    # Only consider primes with at least 4 digits.
    max_prime = 10**6 - 1  # since N <= 1000000, we only need primes up to 999999
    primes = sieve(max_prime)
    groups = {}
    # Group primes by (digit_count, sorted_digits)
    for p in primes:
        s = str(p)
        d = len(s)
        if d < 4:
            continue
        key = (d, tuple(sorted(s)))
        groups.setdefault(key, []).append(p)
    # For each group with at least K members, try to find K-term AP's.
    seq_set = set()
    for key, plist in groups.items():
        if len(plist) < K:
            continue
        plist.sort()
        pset = set(plist)
        # For each pair (a,b) in plist with a < b, let diff = b - a.
        # Then candidate sequence is [a, a+diff, a+2*diff, ..., a+(K-1)*diff].
        m = len(plist)
        for i in range(m):
            a = plist[i]
            # first element must be less than N
            if a >= N:
                continue
            for j in range(i + 1, m):
                b = plist[j]
                diff = b - a
                candidate = [a + diff * k for k in range(K)]
                # The candidate must be entirely within the same digit length.
                # Since the primes in the group have the same number of digits,
                # the last term must be less than 10^d.
                d = key[0]
                if candidate[-1] >= 10**d:
                    continue
                valid = True
                for num in candidate:
                    if num not in pset:
                        valid = False
                        break
                if valid:
                    seq_set.add(tuple(candidate))
    # Sort sequences by their first element (and then lexicographically)
    seq_list = sorted(seq_set, key=lambda s: (s[0], s))
    return seq_list

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    try:
        N = int(data[0])
        K = int(data[1])
    except:
        sys.exit("Invalid input format")
    seq_list = find_sequences(N, K)
    # Print each sequence as concatenated integer
    output_lines = []
    for seq in seq_list:
        # Each term is converted to string and then concatenated.
        s = "".join(str(num) for num in seq)
        output_lines.append(s)
    sys.stdout.write("\n".join(output_lines))

# --------------------- Testing Harness ---------------------

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
    # Sample input: 2000 3 should produce "148748178147" as the only sequence,
    # since 1487, 4817, 8147 is the known sequence with first element less than 2000.
    input_data = "2000 3"
    expected_output = "148748178147"
    output = run_io_fun(input_data, solve)
    assert output == expected_output, "Positive test failed: expected '" + expected_output + "', got '" + output + "'"
    print("Positive test passed.")

    # Negative Test:
    # Choose N such that no sequence has a first term less than N.
    # For example, if N is very low (say 1000) there are no 4-digit primes.
    input_data = "1000 3"
    output = run_io_fun(input_data, solve)
    # We expect an empty output.
    assert output == "", "Negative test failed: expected empty output, got '" + output + "'"
    print("Negative test passed.")

    # Additional Test:
    # For N=3000, only the sequence starting with 1487 qualifies (1487,4817,8147).
    input_data = "3000 3"
    expected_output = "148748178147"
    output = run_io_fun(input_data, solve)
    assert output == expected_output, "Additional test failed: expected '" + expected_output + "', got '" + output + "'"
    print("Additional test passed.")

    # Performance Test:
    # Worst-case: N=1000000, K=3. This should complete within reasonable time.
    input_data = "1000000 3"
    start = time.time()
    _ = run_io_fun(input_data, solve)
    end = time.time()
    elapsed = end - start
    print("Performance test for N=1000000, K=3 completed in %.3f seconds." % elapsed)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        solve()
