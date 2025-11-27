# ⚡ Newton-Raphson Method Solver

A custom **Numerical Root Finder** implemented in Python. This program finds the root of a non-linear equation using the **Newton-Raphson Method** (also known as Newton's Method). Unlike the Bisection method, this approach uses the function's derivative to approximate the root, often resulting in much faster convergence.

## 🚀 Features

* **Algorithm:** Uses the tangent line at the current guess to estimate the root ($x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$).
* **Target Function:** Currently configured to solve $f(x) = e^x - \sin(x)$.
* **Precision Control:** Iterates until the value is within a strict tolerance of `1e-7`.
* **Safety Mechanisms:**
    * **Zero Derivative Check:** Prevents division by zero errors if $f'(x) = 0$.
    * **Iteration Limit:** Stops after 100 iterations to prevent infinite loops if the function diverges.

## 🛠️ Algorithm Specifications

The solver relies on the following logic defined in the script:

| Category | Logic / Formula |
| :--- | :--- |
| **Formula** | $x_{new} = x_{old} - \frac{f(x_{old})}{f'(x_{old})}$ |
| **Target Function `f(x)`** | `np.exp(x) - np.sin(x)` |
| **Derivative `df(x)`** | Calculated in code (User defined) |
| **Tolerance** | `1e-7` |
| **Stop Condition** | When `abs(f(c)) < tol` |

## 📂 Project Structure

The project consists of a single Python script:

1.  **`main.py`**: Contains the function definitions (`f(x)` and `df(x)`), the Newton-Raphson loop, and user input handling.

## 💻 How to Run

### 1. Install Dependencies
This project requires **NumPy**. If you don't have it, install it via pip:

```bash
pip install numpy
```

### 2. Run
Execute the python file in your terminal:
```text
Newton-Ropsen-Method.py
```
  * **‼️Note:** Change Function ***`f(x)`***  and ***`df(X)`*** in the code according to your requirements.

### 3. Input
The program will ask for a single initial guess (x0) to start the iteration process.
```bash
Enter initial guess x0:
```

## 📝 Example 
### UsageScenario: 
Finding the root for **$e^x - \sin(x)$** starting at -1.

#### Console Input:
```bash
Enter initial guess x0: -1
```

#### Generated Output:
```text
Root found at x = -3.183063011933363 after 5 iterations
```
**Note:** Notice how this method often finds the root in fewer iterations compared to the Bisection method for the same accuracy.

## ⚠️ Requirements
* **Python 3.x**
* **NumPy Library** (import numpy)
