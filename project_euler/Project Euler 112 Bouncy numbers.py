import sys

def is_bouncy(x):
    # For x < 100, by definition no number is bouncy.
    if x < 100:
        return False
    s = str(x)
    inc = True
    dec = True
    # Check adjacent digits.
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            dec = False
        elif s[i] < s[i-1]:
            inc = False
        if not inc and not dec:
            return True
    return False

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    # Each test case: two integers n and m. We want the least X such that:
    #     (bouncy_count * m) >= (n * X)
    # We'll sort queries by target ratio (n/m) in increasing order.
    queries = []
    pos = 1
    for i in range(t):
        n = int(data[pos]); m = int(data[pos+1])
        pos += 2
        ratio = n / m  # for typical Euler-style thresholds (e.g., 0.5, 0.9) this is safe
        queries.append((ratio, n, m, i))
    queries.sort(key=lambda x: x[0])
    
    ans = [None] * t
    X = 99
    bouncy_count = 0
    qi = 0  # pointer into sorted queries
    # Sweep X upward until all queries have been answered.
    while qi < t:
        X += 1
        if is_bouncy(X):
            bouncy_count += 1
        # For the current smallest query, check if condition holds:
        #     bouncy_count * m >= n * X
        while qi < t and (bouncy_count * queries[qi][2] >= queries[qi][1] * X):
            # Record answer for this query (using its original index)
            ans[queries[qi][3]] = X
            qi += 1
    sys.stdout.write("\n".join(map(str, ans)) + "\n")

if __name__ == '__main__':
    main()
