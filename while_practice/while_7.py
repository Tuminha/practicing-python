# Difficulty: 🔴 (Advanced)
# While Loop Exercise 7: Nested Loops and Complex Data Processing
# 
# Exercise: Use nested while loops to find common elements between two lists
# and perform advanced analysis on the results
# 1. Use outer while loop to iterate through list_1
# 2. Use inner while loop to search for each element in list_2
# 3. When a common element is found, check if it meets additional criteria
# 4. Count and collect elements that are: common, even, and greater than 5
# 5. Calculate statistics on the filtered results
# 
# This builds on while_6.py by adding:
# - Nested while loops (loop inside a loop)
# - Complex multi-step data processing
# - Advanced filtering with multiple criteria
# - Statistical analysis of results

list_1 = [2, 8, 12, 7, 15, 4, 9, 11, 6, 14, 3, 18, 4]
list_2 = [4, 8, 12, 16, 20, 3, 9, 15, 6, 18, 22, 1]

# Data structures for storing results
common = []                    # List to store all common elements
common_greater_5_and_even = [] # List to store filtered common elements
common_count = 0              # Counter for total common elements
greater_5_and_even_count = 0 # Counter for filtered elements

# Initialize outer loop counter
i = 0

# Outer while loop: iterate through each element in list_1
while i < len(list_1):
    # Initialize inner loop counter for each outer iteration
    j = 0
    
    # Inner while loop: search for current list_1 element in list_2
    while j < len(list_2):
        # Check if current elements match AND element not already in common list
        if list_1[i] == list_2[j] and list_1[i] not in common:
            # Add common element to results
            common.append(list_1[i])
            common_count += 1
            
            # Apply additional filtering criteria: even AND > 5
            if list_1[i] > 5 and list_1[i] % 2 == 0:
                common_greater_5_and_even.append(list_1[i])
                greater_5_and_even_count += 1
            
            # Exit inner loop to avoid duplicate counting
            break
        
        # Move to next element in list_2
        j += 1
    
    # Move to next element in list_1
    i += 1

# Display comprehensive results
print(f"The common numbers are: {common}")
print(f"The common numbers, even and greater than 5 are: {common_greater_5_and_even}")
print(f"The number of common numbers are: {common_count}")
print(f"The number of evens and greater than 5 are: {greater_5_and_even_count}")

