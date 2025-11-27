# Newton-Raphson Method to find root of a function

# Importing necessary libraries
import numpy as np
import sys


def f(x): return np.exp(x) - np.sin(x)  # Function definition
# Function can be changed as per question requirement


def df(x): return np.exp(x) * np.log(1e1) - \
    np.cos(x)  # Derivative of the function
# Derivative will change as per function


a = float(input("Enter initial guess x0: "))  # Taking initial guess from user
tol = 1e-7  # Tolerance
n = 100  # Maximum number of iterations
i = 1  # Iteration counter

while i <= n:
    fa = f(a)
    dfa = df(a)
    if dfa == 0:
        print("Derivative is zero. No solution found.")
        sys.exit()
    c = a - fa / dfa  # Newton-Raphson Formula
    fc = f(c)  # Function value at c
    if abs(fc) < tol:
        # Root found
        sys.exit(print(f"Root found at x = {c} after {i} iterations"))
    a = c  # Update guess
    i += 1

if i > n:
    print("Maximum iterations reached without finding root")
