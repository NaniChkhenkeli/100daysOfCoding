def add(n1, n2):
    return n1 + n2 

def substract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-":substract,
    "*":multiply,
    "/":divide
} 

num1 = int(input("what's the first number? "))
num2 = int(input("what's the second number? "))

for symbol in operations:
    print(symbol)
operation_symbol = input("pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2) 
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("pick another operation: ") 
num3 = int(input("what's the next number? ")) 
calculation_function = operations[operation_symbol] 
second_answer = calculation_function(calculation_function(num1, num2), num3)


print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")







