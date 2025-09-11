# Difficulty: 🟢 (Beginner)
# Functions Exercise 1: Introduction to Functions
# 
# Exercise: Learn the fundamentals of Python functions
# 1. Create basic functions with parameters and return values
# 2. Understand function scope and local variables
# 3. Practice function calls and argument passing
# 4. Learn about default parameters and keyword arguments
# 5. Explore function documentation with docstrings
# 
# This introduces:
# - Function definition syntax (def keyword)
# - Parameters and arguments
# - Return statements and values
# - Function calls and execution
# - Local vs global variable scope
# - Default parameter values
# - Keyword arguments
# - Basic docstring documentation

# =============================================================================
# PART 1: Basic Function Definition and Calling
# =============================================================================

def greet_person(name):
    """
    Greets a person with a friendly message.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

# Test the function
name = "John"
greeting_today = greet_person(name)
print(f"Today's greeting: {greeting_today}")

# =============================================================================
# PART 2: Multi-Parameter Functions
# =============================================================================

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    area = length * width
    return area

# Test the function
length = 10
width = 5
rectangle_area = calculate_area(length, width)
print(f"The area of the rectangle is {rectangle_area}")

# =============================================================================
# PART 3: Boolean Return Functions
# =============================================================================

def is_even(number):
    """
    Checks if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if even, False if odd
    """
    return number % 2 == 0

# Test the function
number = 2
even_check = is_even(number)
print(f"Is the number {number} even? {even_check}")

# =============================================================================
# PART 4: Functions with Default Parameters
# =============================================================================

def create_profile(name, age=18, city="Unknown"):
    """
    Creates a profile with default values for optional parameters.
    
    Args:
        name (str): The person's name
        age (int, optional): The person's age. Defaults to 18.
        city (str, optional): The person's city. Defaults to "Unknown".
        
    Returns:
        tuple: A tuple containing (name, age, city)
    """
    return name, age, city

# Test with all parameters
name_1 = "John"
age_1 = 14
city_1 = "Guimarães"
profile_full = create_profile(name_1, age_1, city_1)
print(f"Full profile: {profile_full[0]}, {profile_full[1]} years old, from {profile_full[2]}")

# Test with default parameters
profile_default = create_profile("Alice")
print(f"Default profile: {profile_default[0]}, {profile_default[1]} years old, from {profile_default[2]}")

# =============================================================================
# PART 5: Local vs Global Scope Demonstration
# =============================================================================

# Global variable (accessible everywhere)
global_calculation = 2 * 8

def scope_demo(local_var):
    """
    Demonstrates the difference between local and global variables.
    
    Args:
        local_var (str): A local variable passed as parameter
        
    Returns:
        str: Information about variable scope
    """
    # Local variable (only accessible within this function)
    local_result = local_var * 2
    
    return f"Global variable: {global_calculation}, Local variable: {local_result}"

# Test the scope demonstration
scope_info = scope_demo(8)
print(f"Scope demonstration: {scope_info}")

# =============================================================================
# PART 6: Comprehensive Function Testing
# =============================================================================

print("\n" + "=" * 60)
print("COMPREHENSIVE FUNCTION TESTING")
print("=" * 60)

# Test all functions with different arguments
print("1. Greeting function:")
print(f"   {greet_person('Luis')}")
print(f"   {greet_person('Maria')}")

print("\n2. Area calculation:")
print(f"   Rectangle 8x3: {calculate_area(8, 3)}")
print(f"   Rectangle 12x7: {calculate_area(12, 7)}")

print("\n3. Even number check:")
print(f"   Is 1 even? {is_even(1)}")
print(f"   Is 4 even? {is_even(4)}")
print(f"   Is 7 even? {is_even(7)}")

print("\n4. Profile creation:")
print(f"   Full profile: {create_profile('Francisco', 46, 'Guimarães')}")
print(f"   Partial profile: {create_profile('Ana', 25)}")
print(f"   Name only: {create_profile('Bob')}")

print("\n5. Scope demonstration:")
print(f"   {scope_demo(6)}")
print(f"   {scope_demo(10)}")

print("\n" + "=" * 60)
print("Functions Exercise 1 Complete! 🎉")
print("=" * 60)





