# Difficulty: 🟡 (Intermediate)
# While Loop Exercise 4: Searching for a Target
# 
# Exercise: Use a while loop to search for a specific number in a list
# 1. Go through each number in the list
# 2. Check if the current number matches your target
# 3. If found, print the position (index) where it was found
# 4. If not found after checking all numbers, print "Not found"
# 
# This builds on while_3.py by adding:
# - Searching for a specific value
# - Early exit when target is found
# - Handling "not found" cases

# Data to search through
numbers = [7, 12, 3, 8, 15, 4, 9, 11, 6]
target = 8  # The number we're looking for

# Initialize search index
i = 0
# Main while loop - search through the list
while i < len(numbers):
    # Check if current element matches our target
    if numbers[i] == target:
        print(f"Target number is {target} and it was found in position index {i}")
        break  # Exit loop early when found
    # Move to next element
    i += 1

# Check if target was not found (loop completed without break)
if i == len(numbers):
    print("Not found")
