# Difficulty: 🟢🟢🟢 (Easy-Intermediate)
# For Loop Exercise 3: Nested For Loops and Complex Data Structures
# 
# Exercise: Use nested for loops to process complex data structures
# 1. Process a 2D list (matrix) using nested for loops
# 2. Compare nested for loops with your while loop matrix experience
# 3. Use for loops to process a list of dictionaries
# 4. Implement data aggregation and analysis patterns
# 5. Explore performance differences between for and while loops
# 
# This builds on for_2.py by adding:
# - Nested for loop patterns
# - Complex data structure processing
# - Dictionary iteration and manipulation
# - Data aggregation techniques
# - Performance considerations

# Complex data structures to work with
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [92, 88, 95]},
    {"name": "Charlie", "age": 19, "grades": [76, 82, 80]},
    {"name": "Diana", "age": 21, "grades": [89, 91, 87]}
]

# Initialize variables for data collection
row_sums = []
column_sums = []
student_averages = []
student_ages = []
high_performers = []

# 1. Process matrix using nested for loops (compare with while_8.py)
print("=== MATRIX ANALYSIS (FOR LOOPS) ===")

# Calculate row sums
print("Row Analysis:")
for i, row in enumerate(matrix):
    row_sum = 0
    for element in row:
        row_sum += element
    row_sums.append(row_sum)
    print(f"Row {i} sum: {row_sum}")

# Calculate column sums
print("\nColumn Analysis:")
for col_index in range(len(matrix[0])):
    column_sum = 0
    for row_index in range(len(matrix)):
        column_sum += matrix[row_index][col_index]
    column_sums.append(column_sum)
    print(f"Column {col_index} sum: {column_sum}")

# 2. Process students data: find average grade for each student
print("\n=== STUDENT ANALYSIS ===")

for student in students:
    name = student["name"]
    grades = student["grades"]
    age = student["age"]
    
    # Calculate student's average grade
    average_grade = sum(grades) / len(grades)
    student_averages.append(average_grade)
    student_ages.append(age)
    
    print(f"Student {name}: Average = {average_grade:.2f}, Age = {age}")
    
    # 3. Find students with average grade > 85
    if average_grade > 85:
        high_performers.append(name)
        print(f"  → {name} is a high performer! 🌟")

# 4. Calculate class statistics
print("\n=== CLASS STATISTICS ===")

# Age statistics
max_age = max(student_ages)
min_age = min(student_ages)
average_age = sum(student_ages) / len(student_ages)

# Grade statistics
overall_average = sum(student_averages) / len(student_averages)

print(f"Age Statistics:")
print(f"  Youngest: {min_age} years old")
print(f"  Oldest: {max_age} years old")
print(f"  Average age: {average_age:.2f} years")

print(f"\nGrade Statistics:")
print(f"  Overall class average: {overall_average:.2f}")
print(f"  High performers (>85): {', '.join(high_performers)}")

# 5. Print comprehensive analysis comparing for vs while approaches
print("\n=== FOR vs WHILE COMPARISON ===")
print("For loops advantages:")
print("  ✓ Cleaner syntax - no manual counter management")
print("  ✓ Automatic iteration over collections")
print("  ✓ Less error-prone (no infinite loops)")
print("  ✓ More Pythonic and readable")

print("\nWhile loops advantages:")
print("  ✓ More control over iteration conditions")
print("  ✓ Better for complex termination logic")
print("  ✓ Can handle dynamic data structures")