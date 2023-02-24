from sympy import *

x = symbols("x")


# Differentiation
def differentiate(expression, x):
    return diff(expression, x)


# Integration
def calculate_integrate(expression, x):
    return integrate(expression, x)


# Get the user input
expression = input("Enter an expression in terms of x: ")

# Check if user input includes multiplication operator
if expression.isalpha() or " " in expression:
    print(
        "Please include the multiplication operator (*) between coefficients and variables."
    )
    expression = input("Enter an expression in terms of x: ")

# Replace caret operator with double asterisk for exponentiation
expression = expression.replace("^", "**")

# Differentiate the expression
derivative = differentiate(expression, x)
print(f"The derivative of {expression} with respect to x is {derivative}")

# Integrate the expression
integral = calculate_integrate(expression, x)
print(f"The indefinite integral of {expression} with respect to x is {integral}")

# Compute the definite integral
a = input("Enter the lower limit of integration (or press Enter to skip): ")
b = input("Enter the upper limit of integration (or press Enter to skip): ")
if a and b:
    definite_integral = calculate_integrate(expression, (x, a, b))
    print(
        f"The definite integral of {expression} from {a} to {b} is {definite_integral}"
    )
elif a or b:
    print(
        "Please enter both the lower and upper limits of integration to compute a definite integral."
    )
