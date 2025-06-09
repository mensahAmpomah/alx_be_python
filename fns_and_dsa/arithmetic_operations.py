# Defining a function

def perform_operation(num1,num2,operation):
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
        results = num1 / num2
        return results
    else:
        print('Enter the correct operation')
