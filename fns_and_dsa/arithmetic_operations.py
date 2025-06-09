# Defining a function

def perform_operation(num1, num2, operation):
    results = 0
    if operation == 'add':
        results = num1 + num2
        return results
    elif operation == 'subtract':
        results = num1 - num2
        return results
    elif operation == 'multiply':
        results = num1 * num2
        return results
    elif operation == 'divide':
        if num1 != 0 & num2 != 0: 
            results = num1 / num2
            return results
        elif num2 == 0:
            print('You entered zero as the second number which is not possible in division.')
            return results
    else:
        print('Enter the correct operation')
