def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Take input from the user
try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
