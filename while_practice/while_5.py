# Difficulty: 🟡🟡 (Intermediate)
# While Loop Exercise 5: Counting Multiple Conditions
# 
# Exercise: Use a while loop to analyze a list and count different types of numbers
# 1. Count how many numbers are even (divisible by 2)
# 2. Count how many numbers are odd (not divisible by 2)
# 3. Count how many numbers are greater than 10
# 4. Print all three counts
# 
# This builds on while_4.py by adding:
# - Multiple counting variables
# - Different types of conditions
# - Using modulo operator (%) for even/odd checking

# Data to analyze
numbers = [3, 8, 12, 7, 15, 4, 9, 11, 6, 14, 2, 18]

# Initialize three separate counters
even_count = 0           # Count of even numbers
odd_count = 0            # Count of odd numbers
greater_than_10_count = 0 # Count of numbers > 10

# Initialize loop counter
i = 0
# Main while loop - analyze each number
while i < len(numbers):
    # Check if number is even (divisible by 2)
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    # Check if number is greater than 10 (independent condition)
    if numbers[i] > 10:
        greater_than_10_count += 1
    
    # Move to next element
    i += 1

# Display all counts
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Numbers greater than 10: {greater_than_10_count}")


