# Functions and Outputs

# CALCULATOR:

# Add
def add(n1, n2):
    return n1 + n2
# subtract
def subtract(n1, n2):
    return n1 - n2
# multiply
def multiply(n1, n2):
    return n1 * n2
# divide
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
num1 = int(input("What's the first number?:"))
num2 = int(input("What's the second number?:"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above:")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(answer)
continue_operation = input("Do you want to carry on with your calculation(yes/no)?").capitalize()
for 'Yes' in continue_operation: 
    if continue_operation is 'Yes':
        num3 = input("Type your next number:")
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above:")
        calculation_function = operations[operation_symbol]
        answer_2 =calculation_function(answer, num3)
        print(answer_2)
else:
    answer = 0
