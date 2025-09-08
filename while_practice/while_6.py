# Difficulty: 🟡🟡🟡 (Intermediate-Advanced)
# While Loop Exercise 6: Building a New List
# 
# Exercise: Use a while loop to create a new list containing only numbers that meet certain criteria
# 1. Go through each number in the original list
# 2. If a number is both even AND greater than 5, add it to a new list
# 3. Print the original list and the new filtered list
# 
# This builds on while_5.py by adding:
# - Creating and modifying lists (not just counting)
# - Using .append() method correctly
# - Combining multiple conditions with AND logic
# - Building new data structures

# Data to filter
numbers = [2, 7, 4, 9, 12, 3, 8, 15, 6, 11, 14, 1]

# Initialize empty list to store filtered results
filtered_numbers = []

# Initialize loop counter
i = 0
# Main while loop - process each number
while i < len(numbers):
    # Check if number meets BOTH criteria: even AND > 5
    if numbers[i] % 2 == 0 and numbers[i] > 5:
        filtered_numbers.append(numbers[i])  # Add to filtered list
    # Move to next element
    i += 1

# Display both original and filtered results
print("Original list:", numbers)
print("Filtered list (even AND > 5):", filtered_numbers)
