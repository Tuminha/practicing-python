# Difficulty: 🟢🟢 (Easy)
# While Loop Exercise 2: Sum and Count
# 
# Exercise: Use a while loop to go through a list and:
# 1. Count how many numbers are greater than 5
# 2. Calculate the sum of all numbers greater than 5
# 3. Print both the count and the sum
# 
# This builds on while_1.py by adding:
# - Keeping track of a running total (sum)
# - Counting specific items
# - Using variables to store results

# Data to analyze
numbers = [2, 7, 3, 9, 1, 8, 4, 6, 5]

# Initialize counters for tracking results
count = 0  # Count of numbers > 5
sum = 0    # Sum of numbers > 5

# Initialize loop counter
i = 0
# Main while loop - iterate through all numbers
while i < len(numbers):
    # Check if current number is greater than 5
    if numbers[i] > 5:
        count += 1        # Increment counter
        sum += numbers[i] # Add to running total
    # Move to next element
    i += 1

# Display results
print(f"The loop has finished with {i} iterations")
print(f"The count of numbers greater than 5 is {count}")
print(f"The sum of numbers greater than 5 is {sum}")

