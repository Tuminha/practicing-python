"""
Functions Practice #3: Recursion, Lambda Functions, and Decorators
================================================================

Difficulty: 🟢🟢🟢 Easy-Intermediate
Topics Covered:
- Recursive functions and base cases
- Lambda (anonymous) functions
- Function decorators (@decorator syntax)
- Decorator patterns and use cases
- Built-in decorators (@property, @staticmethod, @classmethod)

Learning Objectives:
- Master recursive programming patterns
- Understand when to use lambda vs regular functions
- Implement custom decorators for function enhancement
- Apply decorators for caching, logging, and validation
- Deepen understanding of Python's function model
"""

# =============================================================================
# PART 1: Recursive Functions - Your Code Goes Here
# =============================================================================
# 
def factorial(n):
    """
    Recursive function to calculate the factorial of n.
    Args:
        n (int): The number to calculate the factorial for.
    Returns:
        int: The factorial of n.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test your factorial function
# Uncomment and fill in the test cases
print("Factorial Tests:")
print(f"factorial(0) = {factorial(0)}")  # Should be 1
print(f"factorial(5) = {factorial(5)}")  # Should be 120

# =============================================================================
# PART 2: Advanced Recursion - Fibonacci Sequence
# =============================================================================
#
# Instructions:
# 1. Create a recursive fibonacci function:
#    Function name: fibonacci
#    Parameters: position (integer)
#    Logic: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
#           Base cases: fibonacci(0) = 0, fibonacci(1) = 1
#    Return: nth fibonacci number
#
# 2. Test with values 0-8

def fibonacci(position):
    """
    Recursive function to calculate the nth Fibonacci number.
    Args:
        position (int): The position in the Fibonacci sequence.
    Returns:
        int: The Fibonacci number at the given position.
    """
    if position == 0:
        return 0
    elif position == 1:
        return 1
    elif position < 1:
        return 0
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)

# Uncomment to test your fibonacci function
print("Fibonacci Tests:")
for i in range(9):
    print(f"fibonacci({i}) = {fibonacci(i)}")

# =============================================================================
# PART 3: Lambda Functions - Anonymous Functions
# =============================================================================
#
# Instructions:
# 1. Create lambda functions for basic math operations:
#    - add_numbers: takes 2 parameters and adds them
#    - square_number: takes 1 parameter and squares it
#    - is_even: takes 1 parameter and returns True if even, False if odd
#
# 2. Use lambda with built-in functions:
#    - Use filter() with lambda to get even numbers from a list
#    - Use map() with lambda to square all numbers in a list
#    - Use sorted() with lambda to sort items by their length

# Your lambda functions go here
add_numbers = lambda x, y: x + y
square_number = lambda x: x ** 2
is_even = lambda x: x % 2 == 0

# Test data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ["apple", "kiwi", "banana", "grape"]

# Your tests go here
print("Lambda Tests:")
print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
print(f"square_number(4) = {square_number(4)}")

# Filter even numbers (use lambda)
even_numbers = list(filter(is_even, numbers))
print(f"Even Numbers: {even_numbers}")

# Square all numbers (use lambda)
squares = list(map(square_number, numbers))
print(f"Square Numbers: {squares}")


# Sort fruits by length (use lambda)
sorted_by_length = sorted(fruits, key=lambda fruit: len(fruit))
print(f"Sorted by length: {sorted_by_length}")

# =============================================================================
# PART 4: Custom Decorators - Your First Decorator
# =============================================================================
#
# Instructions:
# 1. Create a simple decorator called 'timer':
#    - It should print the function name before calling it
#    - It should print "Function completed!" after calling it
#    - Hints: 
#      - Create a wrapper function inside the decorator
#      - Use func.__name__ to get function name
#      - Don't forget to return the wrapper function
#
# 2. Apply the decorator to a test function:
#    - Create a function called 'slow_add' that adds two numbers
#    - Add 'import time' and 'time.sleep(0.5)' to make it slow
#    - Apply the @timer decorator to it

def timer(func):
    def wrapper(*args, **kwargs):
        # *args, **kwargs means "accept any arguments"
        print(f"Starting {func.__name__}...")  # Before
        result = func(*args, **kwargs)          # Call original
        print("Function completed!")           # After
        return result
    return wrapper

# Your test function with decorator goes here
@timer
def slow_add(a, b):
     import time
     time.sleep(0.5)
     return a + b

# Test your decorator
result = slow_add(3, 5)
print(f"Result: {result}")

# =============================================================================
# PART 5: Property Decorator - Custom Class
# =============================================================================
#
# Instructions:
# 1. Create a Rectangle class:
#    - Constructor: __init__(self, width, height)
#    - Instance variables: self.width, self.height
#
# 2. Add property decorators:
#    - @property for 'area' (calculated as width * height)
#    - @property for 'perimeter' (calculated as 2 * (width + height))
#    - @property for 'is_square' (returns True if width == height)
#
# 3. Test your Rectangle class

class Rectangle:
    def __init__(self, width, height):
        # Your constructor code goes here
        self.width = width
        self.height = height 
    
    @property
    def area(self):
        # Your property code goes here
        return self.width * self.height
    
    @property
    def perimeter(self):
        # Your property code goes here
        perimeter_calculation = 2 * (self.width + self.height)
        return perimeter_calculation
    
    @property
    def is_square(self):
        # Your property code goes here
        return self.width == self.height

    @staticmethod
    def validate_dimensions(length):
        """Check if length is positive"""
        return length > 0
    
    @classmethod
    def from_square(cls, side):
        """Create a square rectangle"""
        return cls(side, side)  # cls means "this class"
    
    @classmethod
    def get_description(cls):
        """Return description of this class"""
        return "This creates rectangles"

# Test your Rectangle class
rect = Rectangle(5, 8)
print("Rectangle: width=5, height=8")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")
print(f"Is square: {rect.is_square}")

# =============================================================================
# PART 6: Static and Class Methods - Advanced Class Features
# =============================================================================
#
# Instructions:
# 1. Add methods to your Rectangle class:
#    - @staticmethod validate_dimensions(length): returns True if length > 0
#    - @classmethod from_square(cls, side): creates Rectangle(side, side)
#    - @classmethod get_description(cls): returns "This creates rectangles"
#
# 2. Test the static and class methods

# Add these methods to your Rectangle class above

# Test static and class methods
print(Rectangle.validate_dimensions(5))  # Should be True
print(Rectangle.validate_dimensions(-2)) # Should be False
square_rect = Rectangle.from_square(6)
print(f"Square rectangle: {square_rect.width}x{square_rect.height}")
print(Rectangle.get_description())

# =============================================================================
# PART 7: Comprehensive Testing - Your Choice!
# =============================================================================
#
# Comprehensive Testing for Functions Practice #3

print("=" * 60)
print("COMPREHENSIVE TESTING FOR FUNCTIONS PRACTICE #3")
print("=" * 60)

# --- 1. Test all your functions with various inputs ---

print("\nTesting factorial function:")
test_values = [0, 1, 5, 10]
for val in test_values:
    print(f"factorial({val}) = {factorial(val)}")

# Edge case: negative input
try:
    print("factorial(-1) =", factorial(-1))
except RecursionError:
    print("factorial(-1) caused a RecursionError (as expected for negative input)")

# --- 2. Test fibonacci function with various inputs and edge cases ---



print("\nTesting fibonacci function:")
fib_test_values = [0, 1, 5, 10]
for val in fib_test_values:
    print(f"fibonacci({val}) = {fibonacci(val)}")

# Edge case: large input (should be slow, so we just show the warning)
try:
    print("fibonacci(20) =", fibonacci(20))
except RecursionError:
    print("fibonacci(20) caused a RecursionError (unexpected for n=20)")

# Edge case: negative input
print("fibonacci(-5) =", fibonacci(-5))  # Should be 0

# --- 3. Demonstrate lambda functions with different data ---

print("\nTesting lambda functions:")


print(f"add(3, 4) = {add_numbers(3, 4)}")
print(f"is_even(10) = {is_even(10)}")
print(f"is_even(7) = {is_even(7)}")

# Using lambda with map and filter
nums = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Squared numbers: {squared}")
print(f"Even numbers: {evens}")



# --- 5. Create several Rectangle objects and test all methods ---

print("\nTesting Rectangle class:")

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 5)
rect3 = Rectangle.from_square(7)

rectangles = [rect1, rect2, rect3]
for i, rect in enumerate(rectangles, 1):
    print(f"\nRectangle {i}: width={rect.width}, height={rect.height}")
    print(f"  Area: {rect.area}")
    print(f"  Perimeter: {rect.perimeter}")
    print(f"  Is square: {rect.is_square}")

# Test static and class methods
print("\nTesting Rectangle static and class methods:")
print(f"Rectangle.validate_dimensions(10): {Rectangle.validate_dimensions(10)}")
print(f"Rectangle.validate_dimensions(-3): {Rectangle.validate_dimensions(-3)}")
print(f"Rectangle.get_description(): {Rectangle.get_description()}")

# Edge case: Rectangle with zero or negative dimensions
try:
    bad_rect = Rectangle(0, -2)
    print(f"Created Rectangle(0, -2): area={bad_rect.area}, is_square={bad_rect.is_square}")
except Exception as e:
    print(f"Failed to create Rectangle(0, -2): {e}")

print("=" * 60)
print("Functions Exercise 3 Complete! 🎉")
print("=" * 60)