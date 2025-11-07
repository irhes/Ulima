
"""
5.- Una calculadora básica tiene las siguientes operaciones básicas, suma, resta
multiplicación y división, ingresando dos datos (operandos) y generando un
resultado. El usuario debe ingresar la operación, los operandos y la calculadora debe
mostrar el resultado.

"""

a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))
c = input("Ingrese el operando (+, -, *, /): ")

if c == "+":
    print(a + b)
    
elif c == "-":
    print(a - b)
    
elif c == "*":
    print(a * b)
    
elif c == "/":
    print(a / b)
    
else:
    print("Operando no válido")

