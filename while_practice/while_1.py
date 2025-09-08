# Difficulty: 🟢 (Beginner)
# Simple while loop with basic conditions

# Data to work with
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]

# Initialize loop counter
i = 0
# Main while loop - iterate through list_1
while i < len(list_1):
    # Check if current element * 2 is less than 10
    if list_1[i] * 2 < 10:
        print(f"So far, list_1 in index {i} multiplied by 2 is < 10")
    else:
        print(f"list_1 in index {i} multiplied by 2 is >= 10")
    # Move to next element
    i += 1

