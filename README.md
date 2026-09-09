# Gaussian Elimination

A simple implementation of the **Gaussian Elimination algorithm** in Python using NumPy.

Gaussian elimination is a fundamental algorithm used to solve a system of linear equations by transforming the equations into an equivalent upper-triangular form and then solving them using back substitution.

## Tech Stack

* **Python**
* **NumPy**

## Project Structure

```text
Gaussian-Elimination/
│
├── README.md
├── requirements.txt
└── test.py
```

## How to Run

It is recommended to use a virtual environment.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows — Command Prompt:**

```bash
.venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python test.py
```

## Using the Program

The program uses two matrices to represent a system of linear equations:

* `M` represents the **LHS (Left-Hand Side)** — the coefficients of the variables.
* `N` represents the **RHS (Right-Hand Side)** — the constant values.

For example, the following system:

```text
2x + y = 5
 x + 3y = 6
```

can be represented as:

```python
M = np.array([
    [2, 1],
    [1, 3]
])
```

and:

```python
N = np.array([
    [5],
    [6]
])
```

the solution is:

```text
x = 1.8
y = 1.4
```

Here, `M` contains the coefficients of `x` and `y`, while `N` contains the corresponding values on the right-hand side.

You can modify `M` and `N` in `test.py` to solve a different system of linear equations.



## What This Project Demonstrates

* Representing systems of linear equations using matrices
* Row operations
* Back substitution
* Using NumPy for matrix manipulation

# How I implemented it 

- Step 1: Defined a function for reversing rows, so basically whenever we that a pivot element is zero, we exchange that row with another, it makes our algorithm much simpler.
- Step 2: Implemented a function to find the first non-zero element in a column, incase if the pivot element is 0, we can use the function defined in step 1 to reverse both rows
- Step 3: Convert the system into augmented matrix
- Step 4: Define a function to implement echelon form and then perform back-substitution



