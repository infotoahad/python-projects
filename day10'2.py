#Calculator program projecct!
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operations = {
    "+": add,
    "=": sub,
    "*": mul,
    "/": div
}

a1 = int(input("enter the first number: "))
b1 = int(input("enter the second number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick from the above: ")
function = operations[operation_symbol]
answer = function(a1, b1)
print(f"{a1} {operation_symbol} {b1} = {answer}")