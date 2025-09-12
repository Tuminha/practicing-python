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

# =============================================================================
# PART 1: Mixed Parameter Types - Required, Default, *args, **kwargs
# =============================================================================

def create_student(name, age=18, *subjects, **grades):
    """
    Creates a student profile with mixed parameter types.
    
    Args:
        name (str): Student's name (required)
        age (int, optional): Student's age. Defaults to 18.
        *subjects: Variable number of subjects (collected as tuple)
        **grades: Variable number of grade keyword arguments (collected as dict)
        
    Returns:
        dict: Student information dictionary
    """
    return {
        "name": name,
        "age": age,
        "subjects": subjects,
        "grades": grades
    }

# Test the function
student_1 = create_student("John", 20, "Math", "Science", "Spanish", "Geography", 
                          science=5, spanish=10, unknown=2, geography=10)
print(f"Student: {student_1['name']}, Age: {student_1['age']}")
print(f"Subjects: {', '.join(student_1['subjects'])}")
print(f"Grades: {student_1['grades']}")

# =============================================================================
# PART 2: Variable-Length Arguments (*args)
# =============================================================================

def calculate_average(*numbers):
    """
    Calculates the average of variable number of numbers.
    
    Args:
        *numbers: Variable number of numeric arguments
        
    Returns:
        float: Average of all numbers
    """
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Test the function
average_1 = calculate_average(4, 8, 10)
average_2 = calculate_average(1, 2, 3, 4, 5)
print(f"Average of (4, 8, 10): {average_1}")
print(f"Average of (1, 2, 3, 4, 5): {average_2}")

# =============================================================================
# PART 3: Keyword Arguments (**kwargs)
# =============================================================================

def build_profile(**profile_data):
    """
    Builds a formatted profile string from keyword arguments.
    
    Args:
        **profile_data: Variable number of keyword arguments
        
    Returns:
        str: Formatted profile string
    """
    if not profile_data:
        return "No profile data provided"
    
    parts = []
    for key, value in profile_data.items():
        parts.append(f"{key.title()}: {value}")
    
    return ", ".join(parts)

# Test the function
profile_1 = build_profile(name="Francisco", age=46, city="Guimarães", job="Developer")
print(f"Profile: {profile_1}")

# =============================================================================
# PART 4: Function Composition - Multiple Transformations
# =============================================================================

def process_text(text):
    """
    Applies multiple text transformations in sequence.
    
    Args:
        text (str): Input text to process
        
    Returns:
        str: Processed text with multiple transformations applied
    """
    return text.strip().lower().replace(",", "").replace(" ", "_")

# Test the function
text_before = "  HEllO, WORLD,"
text_after = process_text(text_before)
print(f"Original: '{text_before}'")
print(f"Processed: '{text_after}'")

# =============================================================================
# PART 5: Higher-Order Function - Function Factory
# =============================================================================

def create_multiplier(factor):
    """
    Creates a function that multiplies by a given factor.
    
    Args:
        factor (number): The multiplication factor
        
    Returns:
        function: A function that multiplies its argument by the factor
    """
    def multiply(number):
        return number * factor
    return multiply

# Test the function
multiply_by_3 = create_multiplier(3)
multiply_by_5 = create_multiplier(5)
multiply_by_10 = create_multiplier(10)

print(f"3 × 4 = {multiply_by_3(4)}")
print(f"5 × 7 = {multiply_by_5(7)}")
print(f"10 × 2 = {multiply_by_10(2)}")

# =============================================================================
# PART 6: Function as Parameter - Higher-Order Function
# =============================================================================

def apply_operation(operation, data):
    """
    Applies an operation function to a list of data.
    
    Args:
        operation (function): Function to apply to each element
        data (list): List of data to process
        
    Returns:
        list: Result of applying the operation to the data
    """
    return operation(data)

def increment_all(numbers):
    """
    Increments all numbers in a list by 1.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        list: New list with incremented values
    """
    return [num + 1 for num in numbers]

def square_all(numbers):
    """
    Squares all numbers in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        list: New list with squared values
    """
    return [num ** 2 for num in numbers]

# Test the functions
test_data = [1, 2, 3, 4, 5]
incremented = apply_operation(increment_all, test_data)
squared = apply_operation(square_all, test_data)

print(f"Original: {test_data}")
print(f"Incremented: {incremented}")
print(f"Squared: {squared}")

# =============================================================================
# PART 7: Comprehensive Testing and Demonstration
# =============================================================================

print("\n" + "=" * 60)
print("COMPREHENSIVE FUNCTION TESTING")
print("=" * 60)

# Test mixed parameters
print("1. Mixed Parameter Types:")
student_2 = create_student("Maria", 25, "Physics", "Chemistry", "Biology", 
                          physics=9, chemistry=8, biology=10)
print(f"   {student_2}")

# Test variable arguments
print("\n2. Variable Arguments:")
print(f"   Average of 10, 20, 30: {calculate_average(10, 20, 30)}")
print(f"   Average of single number: {calculate_average(42)}")

# Test keyword arguments
print("\n3. Keyword Arguments:")
profile_2 = build_profile(first_name="Ana", last_name="Silva", 
                         department="Engineering", experience=5)
print(f"   {profile_2}")

# Test function composition
print("\n4. Function Composition:")
test_texts = ["  Hello, World!  ", "  PYTHON, PROGRAMMING  "]
for text in test_texts:
    processed = process_text(text)
    print(f"   '{text}' → '{processed}'")

# Test higher-order functions
print("\n5. Higher-Order Functions:")
multipliers = [create_multiplier(i) for i in [2, 4, 6]]
for i, mult_func in enumerate(multipliers, 2):
    result = mult_func(5)
    print(f"   {i} × 5 = {result}")

# Test function as parameter
print("\n6. Function as Parameter:")
operations = [increment_all, square_all]
for op in operations:
    result = apply_operation(op, [1, 2, 3])
    print(f"   {op.__name__}([1, 2, 3]) = {result}")

print("\n" + "=" * 60)
print("Functions Exercise 2 Complete! 🎉")
print("=" * 60)