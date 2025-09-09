# Difficulty: 🟢 (Beginner)
# For Loop Exercise 1: Basic Iteration and Range
# 
# Exercise: Use for loops to iterate through different data structures
# 1. Iterate through a list of numbers using a for loop
# 2. Use range() to generate numbers and iterate through them
# 3. Iterate through a string to process each character
# 4. Compare for loops with while loops (you've mastered while loops!)
# 
# This introduces for loops by building on your while loop knowledge:
# - Simpler syntax than while loops
# - Automatic iteration (no manual counter management)
# - Built-in range() function for number sequences
# - Natural iteration over collections

# Data to work with
numbers = [5, 12, 8, 3, 15, 7, 9]
text = "Hello Python"
target_number = 8

# Your code goes here:
# 1. Iterate through numbers list and print each number
for number in numbers:
    print(number)
# 2. Use range(5) to print numbers 0 to 4
for i in range(5):
    print(i)
# 3. Iterate through text string and print each character
for i in text:
    print(i)
# 4. Search for target_number in the list (like while_4.py but with for loop)
i = 0
while i < len(numbers):
    if numbers[i] == target_number:
        print(f"I found the target Number in position {i}")
        break
    i +=1
# 5. Print a comparison message about for vs while loops
print("For loops are easier and more intuitive than while loops")
