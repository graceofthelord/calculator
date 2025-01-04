name = 'calculator'

print('addition')
print('subtraction')
print('multiplication')
print('division')
print('square root')
print('cube root')
print('square')
print('cube')
print('factorial')
print('combination')
print('permutation')

operation = input('enter any operation for calculation: ').strip().lower()

import math

def addition():
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(f"{x} + {y} = {x + y}")

def subtraction():
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(f"{x} - {y} = {x - y}")

def multiplication():
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(f"{x} * {y} = {x * y}")

def division():
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    if y != 0:
        print(f"{x} / {y} = {x / y}")
    else:
        print('Division by zero is not allowed.')

def square_root():
    number = int(input("enter the number: "))
    print(f"√{number} = {math.sqrt(number)}")

def cube_root():
    number = float(input("enter the number: "))
    print(f"∛{number} = {number ** (1/3)}")

def square():
    number = int(input("enter the number: "))
    print(f"{number}² = {number ** 2}")

def cube():
    number = int(input("enter the number: "))
    print(f"{number}³ = {number ** 3}")

def factorial():
    import math
    x = int(input("enter the number: "))
    print(f"{x}! = {math.factorial(x)}")

def combination():
    n = int(input('enter n: '))
    r = int(input('enter r: '))
    from math import comb
    print(f"C({n}, {r}) = {comb(n, r)}")

def permutation():
    n = int(input('enter n: '))
    r = int(input('enter r: '))
    from math import perm
    print(f"P({n}, {r}) = {perm(n, r)}")

operations = {
    'addition': addition,
    'subtraction': subtraction,
    'multiplication': multiplication,
    'division': division,
    'square root': square_root,
    'cube root': cube_root,
    'square': square,
    'cube': cube,
    'factorial': factorial,
    'combination': combination,
    'permutation': permutation
}

if operation in operations:
    operations[operation]()
else:
    print(f"Invalid operation: {operation}")
