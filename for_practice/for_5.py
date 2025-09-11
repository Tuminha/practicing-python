# Difficulty: 🟡🟡 (Intermediate)
# For Loop Exercise 5: Performance Optimization and Best Practices
# 
# Exercise: Master performance optimization and Pythonic best practices
# 1. Compare performance between different iteration methods
# 2. Optimize code using built-in functions and comprehensions
# 3. Implement efficient data processing patterns
# 4. Use generator expressions for memory efficiency
# 5. Apply best practices for readable and maintainable code
# 
# This builds on for_4.py by adding:
# - Performance analysis and optimization techniques
# - Built-in function usage (sum, max, min, any, all)
# - Generator expressions vs list comprehensions
# - Memory efficiency considerations
# - Pythonic coding best practices
# - Code readability and maintainability

import time
import random

# Generate test data
large_numbers = [random.randint(1, 1000) for _ in range(10000)]
words_list = ["python", "programming", "coding", "algorithm", "function", "variable"] * 1000
matrix_data = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]

# =============================================================================
# PART 1: Performance Comparison - Traditional For Loop vs Built-in Functions
# =============================================================================

print("=" * 60)
print("PART 1: Sum of Squares Performance Comparison")
print("=" * 60)

# Traditional for loop approach
start_time = time.perf_counter()
sum_traditional = 0
for number in large_numbers:
    sum_traditional += number ** 2
end_time = time.perf_counter()
duration_traditional = end_time - start_time

print(f"Traditional for loop:")
print(f"  Execution time: {duration_traditional:.6f} seconds")
print(f"  Result: {sum_traditional:,}")

# Built-in function approach
start_time = time.perf_counter()
sum_comprehensive = sum(number ** 2 for number in large_numbers)
end_time = time.perf_counter()
duration_comprehensive = end_time - start_time

print(f"\nBuilt-in sum() with generator:")
print(f"  Execution time: {duration_comprehensive:.6f} seconds")
print(f"  Result: {sum_comprehensive:,}")

# Performance comparison
speed_improvement = duration_traditional / duration_comprehensive
print(f"\nPerformance Analysis:")
print(f"  Built-in sum() is {speed_improvement:.2f}x faster!")
print(f"  Time saved: {duration_traditional - duration_comprehensive:.6f} seconds")


# =============================================================================
# PART 2: Maximum Value Finding - Manual vs Built-in
# =============================================================================

print("\n" + "=" * 60)
print("PART 2: Maximum Value Finding Comparison")
print("=" * 60)

# Traditional max finding approach
start_time = time.perf_counter()
max_traditional = large_numbers[0]
for number in large_numbers[1:]:
    if number > max_traditional:
        max_traditional = number
end_time = time.perf_counter()
duration_max_traditional = end_time - start_time

print(f"Traditional for loop:")
print(f"  Execution time: {duration_max_traditional:.6f} seconds")
print(f"  Maximum value: {max_traditional}")

# Built-in max function
start_time = time.perf_counter()
max_built_in = max(large_numbers)
end_time = time.perf_counter()
duration_max_builtin = end_time - start_time

print(f"\nBuilt-in max() function:")
print(f"  Execution time: {duration_max_builtin:.6f} seconds")
print(f"  Maximum value: {max_built_in}")

# Verify results match
print(f"\nVerification: Results match = {max_traditional == max_built_in}")

# =============================================================================
# PART 3: Memory Efficiency - List Comprehension vs Generator Expression
# =============================================================================

print("\n" + "=" * 60)
print("PART 3: Memory Efficiency Comparison")
print("=" * 60)

# List comprehension approach
start_time = time.perf_counter()
squares_list = [number ** 2 for number in range(1, 10000)]
end_time = time.perf_counter()
duration_list_comp = end_time - start_time

print(f"List comprehension:")
print(f"  Execution time: {duration_list_comp:.6f} seconds")
print(f"  Memory: Stores all {len(squares_list):,} values")

# Generator expression approach
start_time = time.perf_counter()
total = 0
for square in (x**2 for x in range(10000)):
    total += square
end_time = time.perf_counter()
duration_generator = end_time - start_time

print(f"\nGenerator expression:")
print(f"  Execution time: {duration_generator:.6f} seconds")
print(f"  Memory: Processes one value at a time")
print(f"  Total sum: {total:,}")

print(f"\nMemory Analysis:")
print(f"  List comprehension: Stores all values in memory")
print(f"  Generator: Memory efficient, processes on-demand")

# =============================================================================
# PART 4: Built-in Functions - any() and all() for Efficient Checking
# =============================================================================

print("\n" + "=" * 60)
print("PART 4: Built-in Functions - any() and all()")
print("=" * 60)

# Check if any number > 500
any_large = any(number > 500 for number in large_numbers)
print(f"Any number > 500: {any_large}")

# Check if all numbers > 0
all_positive = all(number > 0 for number in large_numbers)
print(f"All numbers positive: {all_positive}")

# Additional checks
any_even = any(number % 2 == 0 for number in large_numbers)
all_less_than_1000 = all(number < 1000 for number in large_numbers)

print(f"\nAdditional checks:")
print(f"  Any even numbers: {any_even}")
print(f"  All numbers < 1000: {all_less_than_1000}")

# =============================================================================
# PART 5: Matrix Operations - Optimized with Built-in Functions
# =============================================================================

print("\n" + "=" * 60)
print("PART 5: Matrix Operations Optimization")
print("=" * 60)

# Calculate row sums efficiently
row_sums = [sum(row) for row in matrix_data]
max_row_sum = max(row_sums)

print(f"Matrix dimensions: {len(matrix_data)} x {len(matrix_data[0])}")
print(f"Row sums: {row_sums[:5]}... (showing first 5)")
print(f"Maximum row sum: {max_row_sum}")

# Calculate column sums using zip
column_sums = [sum(col) for col in zip(*matrix_data)]
max_col_sum = max(column_sums)

print(f"\nColumn sums: {column_sums[:5]}... (showing first 5)")
print(f"Maximum column sum: {max_col_sum}")

# =============================================================================
# PART 6: Best Practices - Clean, Reusable Functions
# =============================================================================

print("\n" + "=" * 60)
print("PART 6: Best Practices - Clean Functions")
print("=" * 60)

def analyze_matrix(matrix):
    """
    Analyze a matrix and return comprehensive statistics.
    
    Args:
        matrix: 2D list of numbers
        
    Returns:
        dict: Dictionary containing matrix statistics
    """
    row_sums = [sum(row) for row in matrix]
    column_sums = [sum(col) for col in zip(*matrix)]
    
    return {
        'dimensions': (len(matrix), len(matrix[0])),
        'row_sums': row_sums,
        'column_sums': column_sums,
        'max_row_sum': max(row_sums),
        'max_col_sum': max(column_sums),
        'total_elements': len(matrix) * len(matrix[0]),
        'average_value': sum(sum(row) for row in matrix) / (len(matrix) * len(matrix[0]))
    }

# Use the function
matrix_stats = analyze_matrix(matrix_data)
print("Matrix Analysis Results:")
for key, value in matrix_stats.items():
    if key in ['row_sums', 'column_sums']:
        print(f"  {key}: {value[:3]}... (showing first 3)")
    else:
        print(f"  {key}: {value}")

# =============================================================================
# PART 7: Performance Summary and Recommendations
# =============================================================================

print("\n" + "=" * 60)
print("PART 7: Performance Summary and Recommendations")
print("=" * 60)

print("Performance Analysis Summary:")
print(f"  Sum of squares - Built-in sum(): {speed_improvement:.2f}x faster")
print(f"  Max finding - Built-in max(): {duration_max_traditional/duration_max_builtin:.2f}x faster")
print(f"  Memory efficiency - Generator: Memory efficient for large datasets")

print("\nKey Recommendations:")
print("  1. Use built-in functions (sum, max, min) instead of manual loops")
print("  2. Use generator expressions for memory efficiency")
print("  3. Use any() and all() for efficient boolean checks")
print("  4. Write reusable functions with clear documentation")
print("  5. Use list comprehensions for simple transformations")
print("  6. Profile your code to identify actual bottlenecks")

print("\n" + "=" * 60)
print("Exercise Complete! Performance optimization mastered! 🚀")
print("=" * 60)

