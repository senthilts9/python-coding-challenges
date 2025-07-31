# Enter your code here. Read input from STDIN. Print output to STDOUT



def collatz_length(n, memo):
    """
    Returns the length of the Collatz chain starting from n.
    Uses memoization to store results for previously computed numbers.
    """
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
        
    memo[n] = 1 + collatz_length(next_n, memo)
    return memo[n]

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    
    # Number of test cases
    t = int(input_data[0])
    results = []
    
    # Create a dictionary for memoization
    memo = {}
    
    # Process each test case
    for i in range(1, t + 1):
        n = int(input_data[i])
        max_length = 0
        answer = 0
        
        # Iterate over all starting numbers from 1 to n
        for start in range(1, n + 1):
            length = collatz_length(start, memo)
            # If we find a longer chain, or equal chain length but with a larger number, update the answer.
            if length > max_length or (length == max_length and start > answer):
                max_length = length
                answer = start
                
        results.append(answer)
    
    # Output the results for each test case.
    sys.stdout.write("\n".join(map(str, results)))

# The following allows the solution to be run as a script
if __name__ == "__main__":
    solve()
