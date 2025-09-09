# Difficulty: 🔴🔴 (Advanced-Expert)
# While Loop Exercise 8: Matrix Operations and Complex Algorithms
# 
# Exercise: Use nested while loops to perform matrix-like operations on a 2D list
# 1. Create a 2D list (matrix) and process it with nested while loops
# 2. Find the sum of each row and each column
# 3. Identify the row with the maximum sum
# 4. Find elements that are greater than the average of all elements
# 5. Calculate statistics and display comprehensive results
# 
# This builds on while_7.py by adding:
# - 2D list processing (matrix operations)
# - Multiple statistical calculations
# - Complex data analysis algorithms
# - Advanced nested loop patterns

# 2D list (matrix) for processing
matrix = [
    [3, 7, 2, 9],
    [1, 8, 4, 6],
    [5, 2, 8, 3],
    [7, 1, 9, 4]
]

# Initialize variables for matrix analysis
row_sums = []           # Store sum of each row
column_sums = []        # Store sum of each column
all_elements = []       # Store all elements for average calculation
elements_above_avg = [] # Store elements greater than average

# PHASE 1: Calculate sum of each row using nested loops
print("=== ROW ANALYSIS ===")
i = 0
while i < len(matrix):
    j = 0
    row_sum = 0
    
    # Sum all elements in current row
    while j < len(matrix[i]):
        row_sum += matrix[i][j]
        all_elements.append(matrix[i][j])  # Collect for average calculation
        j += 1
    
    row_sums.append(row_sum)
    print(f"Row {i} has sum: {row_sum}")
    i += 1

# PHASE 2: Calculate sum of each column using nested loops
print("\n=== COLUMN ANALYSIS ===")
j = 0
while j < len(matrix[0]):
    i = 0
    column_sum = 0
    
    # Sum all elements in current column
    while i < len(matrix):
        column_sum += matrix[i][j]
        i += 1
    
    column_sums.append(column_sum)
    print(f"Column {j} sum: {column_sum}")
    j += 1

# PHASE 3: Find row with maximum sum
print(f"\n=== MAXIMUM ROW ANALYSIS ===")
max_value = max(row_sums)
max_index = row_sums.index(max_value)
print(f"Row {max_index} has the maximum sum: {max_value}")

# PHASE 4: Calculate average of all elements
print(f"\n=== AVERAGE CALCULATION ===")
total_sum = sum(all_elements)
total_elements = len(all_elements)
average = total_sum / total_elements
print(f"Total elements: {total_elements}")
print(f"Total sum: {total_sum}")
print(f"Average: {average:.2f}")

# PHASE 5: Find elements greater than average
print(f"\n=== ELEMENTS ABOVE AVERAGE ===")
elements_position_above_average = []

# Reset loop counter for matrix traversal
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[0]):
        # Check if current element is above average
        if matrix[i][j] > average:
            elements_above_avg.append(matrix[i][j])
            position = [i, j]
            elements_position_above_average.append(position)
            print(f"Element {matrix[i][j]} at position [{i}][{j}] is above average")
        j += 1
    i += 1

print(f"Elements above average: {elements_above_avg}")
print(f"Positions: {elements_position_above_average}")



# PHASE 6: Display comprehensive statistics
print(f"\n=== COMPREHENSIVE STATISTICS ===")
print(f"Row sums: {row_sums}")
print(f"Column sums: {column_sums}")
print(f"Elements above average ({average:.2f}): {elements_above_avg}")
print(f"Count of elements above average: {len(elements_above_avg)}")
print(f"Maximum row sum: {max_value} (Row {max_index})")
