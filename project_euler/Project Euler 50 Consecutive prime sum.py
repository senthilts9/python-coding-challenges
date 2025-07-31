# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve_of_eratosthenes(N):
    # Generate all primes up to N using the Sieve of Eratosthenes
    is_prime = [True] * (N + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, N + 1) if is_prime[i]]
    return primes

def find_prime_with_longest_consecutive_sum(N):
    # Generate primes up to N
    primes = sieve_of_eratosthenes(N)
    prime_set = set(primes)
    max_length = 0
    max_prime = 0
    
    # Try all possible consecutive prime sums
    for start in range(len(primes)):
        total_sum = 0
        for end in range(start, len(primes)):
            total_sum += primes[end]
            if total_sum > N:
                break  # No need to check further if sum exceeds N
            if total_sum in prime_set and (end - start + 1) > max_length:
                max_length = end - start + 1
                max_prime = total_sum
    
    return max_prime, max_length

def main():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        N = int(input())
        prime, length = find_prime_with_longest_consecutive_sum(N)
        print(f"{prime} {length}")

if __name__ == "__main__":
    main()
