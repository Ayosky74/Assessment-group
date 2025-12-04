def addition(a, b):
    """this adds 2 numbers a,b and returns the sum"""
    return a + b


def subtract(a, b):
    """ this subtracts 2 numbers a,b and returns the  result"""
    return a - b


def multiply(a, b):
    """ these multiples 2 numbers a,b and returns the multiplication"""
    return a * b


def division(a, b):
    if b == 0:
        return "Error! Division bu zero."
    return a / b


def calculate():
    global result
    print("Select operation:")
    print("1. Add (+)")
    print("2.Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4'):
            try:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                result = addition(number1, number2)
            elif choice == '2':
                result = subtract(number1, number2)
            elif choice == '3':
                result = multiply(number1, number2)
            elif choice == '4':
                result = division(number1, number2)

            print("Result:", result)

        elif choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please select a valid operation.")


calculate()
