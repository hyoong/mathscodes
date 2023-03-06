import matplotlib.pyplot as plt
import numpy as np
import math
import re
import tkinter as tk

# Define a regular expression to match allowed input
allowed_expr = re.compile(r'^[-+*/%(),\d\sxpietancoshrlosg]+\Z')

def plot_function(expr_str):
    # Create the dictionary of functions and constants
    expr_dict = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'arcsin': np.arcsin,
        'arccos': np.arccos,
        'arctan': np.arctan,
        'sinh': np.sinh,
        'cosh': np.cosh,
        'tanh': np.tanh,
        'log': np.log,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'pi': math.pi,
        'e': math.e,
        'inf': np.inf,
        'nan': np.nan,
        'real': np.real,
        'imag': np.imag,
        'conj': np.conj
    }

    # Get the range of x values
    xmin, xmax, num = -3, 3, 1000
    x_values = np.linspace(xmin, xmax, num)

    # Evaluate the function for x values
    y_values = eval(expr_str, {'__builtins__': None}, {**expr_dict, 'x': x_values})

    # Set up the plot
    fig, ax = plt.subplots()

    # Plot the function
    ax.plot(x_values, y_values)

    # Set the x and y limits
    ax.set_xlim(xmin, xmax)

    # Set the title and labels
    ax.set_title('Function Plot')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Show the plot
    plt.show()

def submit_expression():
    expr_str = input_entry.get()
    if allowed_expr.match(expr_str):
        plot_function(expr_str)
        output_label.configure(text='')
    else:
        output_label.configure(text='Invalid expression. Please try again.')

# Create the GUI
root = tk.Tk()
root.title("Function Plotter")

# Create the input field
input_label = tk.Label(root, text="Enter a mathematical expression in terms of x:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Plot", command=submit_expression)
submit_button.pack()

# Create the output field
output_label = tk.Label(root)
output_label.pack()

root.mainloop()
