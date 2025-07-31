# Enter your code here. Read input from STDIN. Print output to STDOUT

def number_to_words(n):
    # Base mappings for numbers to words
    below_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                    "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Handle 0 explicitly
    if n == 0:
        return "Zero"

    # Numbers below 20 can be returned directly
    if n < 20:
        return below_twenty[n]
    
    # Numbers 20-99: handle tens and units
    if n < 100:
        return tens[n // 10] + (below_twenty[n % 10] if n % 10 != 0 else "")
    
    # Numbers 100-999: handle hundreds and the rest
    if n < 1000:
        return below_twenty[n // 100] + "Hundred" + (number_to_words(n % 100) if n % 100 != 0 else "")

    # Extend as needed for larger numbers (not required for this problem’s constraints)
    return "NumberOutOfRange"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    T = int(data[0])
    results = []

    for i in range(T):
        n = int(data[i + 1])
        results.append(number_to_words(n))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
