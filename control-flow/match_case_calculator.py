# Match case Calculator.

# Variable for taking the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operations = input("Choose the operation (+,-,*,/): ")

match operations:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        result = num1 / num2
        print(f"The result is {result}.")
    case _:
        print("Cannot divide by zero.")
