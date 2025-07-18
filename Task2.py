# Task 2: Using the Math Module for Calculations
import math

# Asking user for input
number = float(input("\nEnter a number for math operations: "))

# Performing calculations using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Displaying the results
print("\n--- Math Module Calculations ---")
print(f"Square root of {number} = {square_root}")
print(f"Natural logarithm of {number} = {natural_log}")
print(f"Sine of {number} radians = {sine_value}")
