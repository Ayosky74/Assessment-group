# Assessment-group
This is the report for my assessment

# Overview

This project is a menu-driven calculator built in Python.
It demonstrates fundamental programming concepts such as functions, loops, error handling, and user input validation.

The calculator supports the following operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/) with division-by-zero handling
Power (^) using Python’s math.pow()

# Features

* Menu-driven interface for ease of use.
* Handles invalid inputs gracefully (e.g., non-numeric values).
* Prevents division by zero errors.
* Loops continuously until the user chooses to exit.
* Extensible design, which means a new operations can be added easily.


# How It Works

* When you run the program, it displays a menu of operations.
* You select an operation by entering its corresponding number (1–6).
* You then enter two numbers.
* The program performs the chosen operation and prints the result.
* The menu reappears, allowing you to perform more calculations.
* Enter 6 to exit the program.


# How It Runs

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Power(^)
6. Exit
Enter choice (1/2/3/4/5/6): 1
Enter first number: 5
Enter second number: 9
Result: 14.0

Enter choice (1/2/3/4/5/6): 4
Enter first number: 4
Enter second number: 0
Result: Error! Division by zero.

Enter choice (1/2/3/4/5/6): 6
Exiting Calculator. Goodbye!


# Developer Role

* Designed modular functions (add, subtract, multiply, divide, power) for clarity and reuse.
* Implemented a menu-driven loop (calculate()) to allow continuous user interaction.
* Applied error handling (try/except) to prevent crashes from invalid input.
* Structured code for extensibility, making it easy to add new operations.


# Tester Role

# Positive Test Cases:

Addition of two positive numbers; 10 + 5 = 15
Subtraction with negative result; 5 - 10 = -5
Power function with exponent zero; 7 ^ 0 = 1

# Negative Test Cases:

Division by zero returns; "Error! Division by zero."
Non-numeric input like ABC; "Invalid input. Please enter a valid number."


# Future Improvements

* Adding algorithm, square root, factorial, and trigonometric equation/functions.
* Integration of unit testing for automated validation.
* Implement logging to track invalid inputs or errors.
* Building a GUI version.
* Add a history feature to view past calculations.
