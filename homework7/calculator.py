import math_tools

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Which operation? (+, -, * or /): ")
if operation == '+':
    print(math_tools.add(first_number, second_number))
elif operation == '-':
    print(math_tools.subtract(first_number, second_number))
elif operation == '*':
    print(math_tools.multiply(first_number, second_number))
else:
    print(math_tools.divide(first_number, second_number))
