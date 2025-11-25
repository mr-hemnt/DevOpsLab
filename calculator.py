def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation selected!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run the calculator
calculator()