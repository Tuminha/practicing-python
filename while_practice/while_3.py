# Difficulty: 🟢🟢🟢 (Easy-Intermediate)
# While Loop Exercise 3: Finding Maximum and Minimum
# 
# Exercise: Use a while loop to find the largest and smallest numbers in a list
# 1. Go through each number in the list
# 2. Keep track of the largest number you've seen so far
# 3. Keep track of the smallest number you've seen so far
# 4. Print both the maximum and minimum values
# 
# This builds on while_2.py by adding:
# - Comparing each element to find extremes
# - Using variables to store the "best so far" values
# - Initializing with the first element

# Data to analyze
numbers = [15, 3, 8, 22, 1, 9, 17, 4, 12]

# Initialize max and min with first element (smart initialization)
max = numbers[0]
min = numbers[0]

# Start from index 1 since we already used index 0
i = 1
# Main while loop - check remaining elements
while i < len(numbers):
    # Check if current number is new maximum
    if numbers[i] > max:
        max = numbers[i]
    # Check if current number is new minimum
    if numbers[i] < min:
        min = numbers[i]
    # Move to next element
    i += 1

# Display results
print(f"Maximum value: {max}")
print(f"Minimum value: {min}")
