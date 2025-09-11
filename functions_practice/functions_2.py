# Difficulty: 🟢🟢 (Easy)
# Functions Exercise 2: Advanced Parameters and Function Composition
# 
# Exercise: Master advanced function concepts and patterns
# 1. Use keyword arguments and mixed parameter types
# 2. Implement variable-length arguments (*args and **kwargs)
# 3. Practice function composition and chaining
# 4. Create higher-order functions (functions that take/return functions)
# 5. Explore function objects and first-class functions
# 
# This builds on functions_1.py by adding:
# - Keyword arguments and mixed parameter types
# - Variable-length arguments (*args, **kwargs)
# - Function composition and chaining
# - Higher-order functions
# - First-class function concepts
# - Advanced parameter patterns
# - Function objects and callable behavior

# Your code goes here:
# 1. Create a function with mixed parameter types
#    Function name: create_student
#    Parameters: name (required), age (default=18), *subjects, **grades
#    Return: student information dictionary
def create_student(required, default=18, *subjects, **grades):
    return {"Name:": required, "Age:": default, "Subjects:": subjects, "Grades:": grades}

# print(create_student("John", 20, "Math", "Science", "Spanish", "Geography", science = 5, spanish = 10, unknown = 2, geography = 10))
student_1 = create_student("John", 20, "Math", "Science", "Spanish", "Geography", science = 5, spanish = 10, unknown = 2, geography = 10)
print(f"From here now we can print the student name that is {student_1['Name:']} and  with {student_1['Age:']} years old that is studying {student_1['Subjects:']} with the grades {student_1['Grades:']}")
# 2. Create a function that demonstrates *args
#    Function name: calculate_average
#    Parameters: *numbers (variable number of arguments)
#    Return: average of all numbers
def calculate_average(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
        
average_1 = calculate_average(4, 8, 10)

print(f"The average is {average_1}")

# 3. Create a function that demonstrates **kwargs
#    Function name: build_profile
#    Parameters: **profile_data (keyword arguments)
#    Return: formatted profile string

# 4. Create a function composition example
#    Function name: process_text
#    Parameters: text (string)
#    Return: processed text (apply multiple transformations)

# 5. Create a higher-order function
#    Function name: create_multiplier
#    Parameters: factor (number)
#    Return: a function that multiplies by the factor

# 6. Create a function that takes another function as parameter
#    Function name: apply_operation
#    Parameters: operation (function), data (list)
#    Return: result of applying operation to data

# 7. Test all functions with various arguments
#    Demonstrate different ways to call functions
