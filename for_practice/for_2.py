# Difficulty: 🟢🟢 (Easy)
# For Loop Exercise 2: Advanced Iteration and Data Processing
# 
# Exercise: Use for loops to perform data analysis and processing
# 1. Use enumerate() to process a list with both index and value
# 2. Use range() with different parameters (start, stop, step)
# 3. Iterate through multiple lists simultaneously using zip()
# 4. Use for loops to filter and transform data
# 5. Compare for loop efficiency with while loops
# 
# This builds on for_1.py by adding:
# - enumerate() for index-value pairs
# - Advanced range() usage
# - zip() for parallel iteration
# - Data processing patterns
# - Performance considerations

# Data to work with
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
prices = [1.50, 0.80, 2.00, 3.50, 2.25]
quantities = [10, 15, 8, 12, 6]

# Initialize variables for collecting results
fruits_position = ""
fruit_price_quantity = ""
price_high = ""
price_quantity = ""

# 1. Use enumerate() to print each fruit with its position
print("=== FRUIT POSITIONS ===")
for i, fruit in enumerate(fruits):
    fruits_position += f"{fruit} is in position index {i} \n"

# 2. Use range(2, 10, 2) to print even numbers from 2 to 8
print("\n=== EVEN NUMBERS (2 to 8) ===")
for i in range(2, 10, 2):
    print(i)

# 3. Use zip() to print fruit, price, and quantity together
print("\n=== FRUIT INVENTORY ===")
for fruit, price, quantity in zip(fruits, prices, quantities):
    fruit_price_quantity += f"We have {quantity} {fruit}s with the price {price} \n"

# 4. Find fruits with price > 2.00 using for loop
print("\n=== EXPENSIVE FRUITS (>$2.00) ===")
for price, fruit in zip(prices, fruits):
    if price > 2.00:
        price_high += f"This {fruit} costs more than 2.00 with the exact price of {price} \n"

# 5. Calculate total value (price * quantity) for each fruit
print("\n=== TOTAL VALUES ===")
for fruit, price, quantity in zip(fruits, prices, quantities):
    value = price * quantity
    price_quantity += f"This {fruit} total value is {value} \n"

# 6. Print a comprehensive summary of findings
print("\n" + "="*20 + " COMPREHENSIVE SUMMARY " + "="*20)
print(fruits_position)
print(fruit_price_quantity)
print(price_high)
print(price_quantity)
