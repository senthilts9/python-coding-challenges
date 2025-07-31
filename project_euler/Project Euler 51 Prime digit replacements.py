def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]], is_prime

def generate_family(prime, digit_positions, digit, is_prime):
    family = []
    prime_str = str(prime)
    for replacement_digit in range(10):
        new_number = list(prime_str)
        for pos in digit_positions:
            new_number[pos] = str(replacement_digit)
        new_number_str = ''.join(new_number)
        if new_number_str[0] != '0':  # Avoid leading zeros
            new_number_int = int(new_number_str)
            if new_number_int != prime and is_prime[new_number_int]:
                family.append(new_number_int)
    return family

def find_smallest_prime_family(L, d, n):
    limit = 10**6  # A reasonable limit to find primes.
    primes, is_prime = sieve_of_eratosthenes(limit)

    for prime in primes:
        prime_str = str(prime)
        digit_positions = [i for i, ch in enumerate(prime_str) if ch == str(d)]
        
        if len(digit_positions) < n:
            continue  # Not enough digits to replace
        
        family = []
        for replacement_digit in range(10):
            if replacement_digit == d:
                continue  # Skip replacing with the same digit
            family = generate_family(prime, digit_positions, replacement_digit, is_prime)
            if len(family) >= L:
                family = list(set(family))  # Unique values
                family.append(prime)  # Include the original prime
                family.sort()
                return family[:L]

# Read input
L, d, n = map(int, input().split())
result = find_smallest_prime_family(L, d, n)
# Print the results
print(" ".join(map(str, sorted(result))))
