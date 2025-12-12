import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)


def calculate():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power(^)")
    print("6. Exit")

    while True:

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4','5'):
            try:

                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)

            print("Result:", result)

        elif choice == '6':

            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please select a valid operation.")


calculate()

