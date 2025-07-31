# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def first_ten_digits_of_sum(n, numbers):
    total_sum = sum(int(num) for num in numbers)
    print(str(total_sum)[:10])

if __name__ == "__main__":
    import sys
    
    input_data = sys.stdin.read().strip().split("\n")
    n = int(input_data[0])
    numbers = input_data[1:n+1]
    
    first_ten_digits_of_sum(n, numbers)
