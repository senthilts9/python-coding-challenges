# Enter your code here. Read input from STDIN. Print output to STDOUT

def solve():
    import sys

    data = sys.stdin.read().strip().split()
    # Expect two integers on a single line: N and K
    N, K = map(int, data)

    def digit_signature(num):
        return tuple(sorted(str(num)))
    
    results_found = False

    for x in range(1, N + 1):
        # Get the digit signature of x
        sig_x = digit_signature(x)
        len_x = len(str(x))

        valid = True
        multiples = [x]  # We'll store x, 2x, ... Kx for output

        # Check 2x, 3x, ..., Kx
        for m in range(2, K + 1):
            val = x * m
            # Quick length check to rule out leading-zero or digit-count mismatch
            if len(str(val)) != len_x:
                valid = False
                break
            # Check digit signature
            if digit_signature(val) != sig_x:
                valid = False
                break
            multiples.append(val)
        
        if valid:
            # Print the entire sequence for this x in one line
            # Example format: "125874 251748"
            print(" ".join(map(str, multiples)))
            results_found = True

    # The problem guarantees at least one solution, so no need for fallback if none found.
