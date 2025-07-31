def is_leap(year):
    """Returns True if the given year is a leap year, False otherwise."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def days_in_month(year, month):
    """Returns the number of days in a given month of a given year."""
    if month in {9, 4, 6, 11}:  # September, April, June, November
        return 30
    elif month == 2:  # February
        return 29 if is_leap(year) else 28
    else:
        return 31

def count_sundays_on_first(start_year, start_month, start_day, end_year, end_month, end_day):
    # The initial reference date: 1 Jan 1900 is a Monday
    current_day_of_week = 0  # Monday = 0, Sunday = 6
    count = 0
    
    # Iterate from the start year to the end year
    year = 1900
    month = 1
    
    # Fast forward to the start date
    while (year, month) < (start_year, start_month):
        current_day_of_week = (current_day_of_week + days_in_month(year, month)) % 7
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    # Count Sundays on the first until the end date
    while (year, month) <= (end_year, end_month):
        if current_day_of_week == 6:  # Sunday
            count += 1
        current_day_of_week = (current_day_of_week + days_in_month(year, month)) % 7
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return count

# Input parsing
import sys
input = sys.stdin.read
data = input().strip().split("\n")

T = int(data[0])  # Number of test cases
results = []
for i in range(T):
    start_date = list(map(int, data[1 + 2*i].split()))
    end_date = list(map(int, data[2 + 2*i].split()))
    result = count_sundays_on_first(start_date[0], start_date[1], start_date[2], 
                                    end_date[0], end_date[1], end_date[2])
    results.append(result)

# Output results
for result in results:
    print(result)
