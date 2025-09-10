# Difficulty: 🟡 (Intermediate)
# For Loop Exercise 4: List Comprehensions and Advanced Patterns
# 
# Exercise: Master advanced for loop patterns and introduce list comprehensions
# 1. Use for loops to create new lists (traditional approach)
# 2. Convert for loops to list comprehensions (Pythonic approach)
# 3. Implement filtering and transformation patterns
# 4. Use for loops with conditional logic and multiple operations
# 5. Explore performance and readability differences
# 
# This builds on for_3.py by adding:
# - List comprehensions (Python's elegant way to create lists)
# - Advanced filtering patterns
# - Transformation and mapping operations
# - Performance optimization techniques
# - Pythonic coding practices

# Data to work with
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["python", "programming", "coding", "algorithm", "function", "variable"]
temperatures = [25, 30, 15, 35, 20, 28, 32, 18, 22, 27]

# Your code goes here:
# 1. Create a list of squares using traditional for loop
squares = []
for num in numbers:
    squares.append(num ** 2)
print("Traditional for loop for squares: ", squares)
# 2. Create the same list using list comprehension
squares_comprehension = [num ** 2 for num in numbers]
print("Comprehension squares list: ", squares_comprehension)
# 3. Filter even numbers using traditional for loop
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print("Traditional for loop: ", evens)

# 4. Filter even numbers using list comprehension
evens_comprehension = [num for num in numbers if num % 2 == 0]
print("Comprehensions for evens: ", evens_comprehension)
# 5. Create a list of word lengths using both approaches
word_length = []
for word in words:
    word_length.append(len(word))
print("Traditrional for Loop: ", word_length)
word_length_comprehensive = [len(word) for word in words]
print("The comprehensive list for words length: ", word_length_comprehensive)
# 6. Filter temperatures > 25 using both approaches
high_temperatures = []
for temperature in temperatures:
    if temperature > 25:
        high_temperatures.append(temperature)
print("Traditional for loop for >25 tempearture: ", high_temperatures)

high_temperatures_comprehensive = [temperature for temperature in temperatures if temperature > 25]
print("With comprehesive approach for temperature > 25: ", high_temperatures_comprehensive)
# 7. Create a list of "Hot" or "Cold" based on temperature
hot_tempearture = [temperature for temperature in temperatures if temperature > 25]
cold_tempearture = [temperature for temperature in temperatures if temperature <= 25]
print("Hot Temperatures:", hot_tempearture)
print("Cold Temperatures:", cold_tempearture)
temperature_labels = ["Hot" if temperature >25 else "Cold" for temperature in temperatures]
print("The correct approach to get a list of hot and cold temperatures:", temperature_labels)
# 8. Compare the approaches and print insights
print("=" * 30)
print("      Final Thoughts")
print("-" * 25)
print("Once you get the trick of the comprehensive approach \n you feel that it is a very good replacement for the conventional for loops")
