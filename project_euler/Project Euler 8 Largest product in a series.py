def solve():
    # Number of test cases
    t = int(input().strip())
    
    for _ in range(t):
        # Read n (number of digits) and k (number of consecutive digits)
        n, k = map(int, input().split())
        # Read the digit string
        number = input().strip()
        
        max_product = 0
        
        # Loop through all possible substrings of length k
        for i in range(n - k + 1):
            product = 1
            # Compute the product of the k consecutive digits
            for digit in number[i:i+k]:
                product *= int(digit)
            # Update max_product if a higher product is found
            max_product = max(max_product, product)
        
        # Print the maximum product for the current test case
        print(max_product)

# Call the solve function to execute the solution
solve()
