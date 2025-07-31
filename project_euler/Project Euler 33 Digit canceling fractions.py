# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
from fractions import Fraction

def is_valid_cancellation(num, den, canc_digits):
    str_num, str_den = str(num), str(den)
    
    for digits in permutations(str_num, canc_digits):
        if all(d in str_den for d in digits):
            reduced_num = list(str_num)
            reduced_den = list(str_den)
            
            for d in digits:
                reduced_num.remove(d)
                reduced_den.remove(d)
            
            if reduced_num and reduced_den:
                new_num = int("".join(reduced_num))
                new_den = int("".join(reduced_den))
                
                if new_den != 0 and Fraction(num, den) == Fraction(new_num, new_den):
                    return True
    return False

def find_curious_fractions(n_digits, c_digits):
    start = 10**(n_digits - 1)
    end = 10**n_digits
    
    sum_num, sum_den = 0, 0
    
    for num in range(start, end):
        for den in range(num + 1, end):  # numerator < denominator
            if "0" in str(num)[-c_digits:] or "0" in str(den)[-c_digits:]:
                continue  # Ignore trivial cases
            
            if is_valid_cancellation(num, den, c_digits):
                sum_num += num
                sum_den += den
    
    print(sum_num, sum_den)

# Reading input
n, c = map(int, input().split())
find_curious_fractions(n, c)
