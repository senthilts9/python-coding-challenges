# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_stack_cubes(blocks):
    left, right = 0, len(blocks) - 1
    last_cub = float('inf')  # Start with a very large number

    while left <= right:
        if blocks[left] >= blocks[right]:  # Choose from the left
            current_cub = blocks[left]
            left += 1
        else:  # Choose from the right
            current_cub = blocks[right]
            right -= 1
        
        # Check if we can place this cube on top
        if current_cub > last_cub:
            return "No"
        
        last_cub = current_cub  # Update the last cube placed

    return "Yes"

# Read input
T = int(input())
for _ in range(T):
    input()  # Read n but do nothing with it
    blocks = list(map(int, input().split()))
    result = can_stack_cubes(blocks)
    print(result)
