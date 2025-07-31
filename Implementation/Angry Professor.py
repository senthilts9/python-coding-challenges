def angryProfessor(k, a):
    """Returns 'YES' if class is cancelled, otherwise 'NO'."""
    on_time_students = sum(1 for time in a if time <= 0)  # Count students who arrived on time
    return "YES" if on_time_students < k else "NO"

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split("\n")
    
    t = int(data[0])  # Number of test cases
    index = 1
    
    results = []
    for _ in range(t):
        n, k = map(int, data[index].split())  # Read n (students) and k (threshold)
        a = list(map(int, data[index + 1].split()))  # Read arrival times
        index += 2  # Move to next test case
        
        results.append(angryProfessor(k, a))  # Store result
    
    # Print all results
    print("\n".join(results))
