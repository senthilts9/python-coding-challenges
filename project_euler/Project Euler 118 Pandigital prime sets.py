import sys
import itertools
from functools import lru_cache

# Miller-Rabin test for numbers up to 10^9 using bases 2,7,61.
@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    # Check for small primes
    if n % 2 == 0:
        return n == 2
    # Write n-1 as d * 2^s.
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Test with bases 2,7,61 (deterministic for n < 2^32)
    for a in (2, 7, 61):
        if a % n == 0:
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

# Precompute, for each nonempty mask over digits 1..9, the list of primes 
# that can be formed by permuting the digits corresponding to that mask.
# We use bit positions 0..8 to represent digits 1..9.
prime_map = {}
# There are 2^9 - 1 possible nonempty masks.
digits_full = [str(i) for i in range(1, 10)]
for mask in range(1, 1 << 9):
    # Get the digits corresponding to this mask.
    dig_list = [digits_full[i] for i in range(9) if mask & (1 << i)]
    # Generate all permutations of these digits.
    # (Since the digits are distinct, no duplicate permutations occur.)
    primes_here = []
    for perm in itertools.permutations(dig_list):
        num = int("".join(perm))
        if is_prime(num):
            primes_here.append(num)
    if primes_here:
        prime_map[mask] = primes_here

# A helper to iterate over all nonzero submasks of a mask.
def submasks(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask

# Given a mask (of the digits available in the test case), partition it into
# one or more disjoint submasks (each of which has at least one prime from prime_map)
# and compute all possible sums.
@lru_cache(maxsize=None)
def partition_sums(mask):
    if mask == 0:
        return frozenset({0})
    sums = set()
    # Iterate over all nonempty submasks of mask.
    for sub in submasks(mask):
        if sub in prime_map:
            for p in prime_map[sub]:
                for rest in partition_sums(mask - sub):
                    sums.add(p + rest)
    return frozenset(sums)

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data: 
        return
    T = int(data[0].strip())
    line_no = 1
    out_lines = []
    for _ in range(T):
        s = data[line_no].strip()
        line_no += 1
        # Build mask for the test case.
        # Since s is given in increasing order and contains distinct digits from 1 to 9,
        # we map digit d to bit position (int(d)-1).
        mask = 0
        for ch in s:
            mask |= 1 << (int(ch) - 1)
        sums = partition_sums(mask)
        for total in sorted(sums):
            out_lines.append(str(total))
        out_lines.append("")  # blank line after each test case
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == '__main__':
    main()
