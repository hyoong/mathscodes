from sympy import *

x = symbols('x')

# Differentiation
def differentiate(expression, x):
    return diff(expression, x)

expression = x**2 + x
derivative = differentiate(expression, x)
print(f"The derivative of {expression} with respect to x is {derivative}")

# Integration
def integrate(expression, x):
    return integrate(expression, x)

integral = integrate(expression, x)
print(f"The definite integral of {expression} with respect to x is {integral}")
