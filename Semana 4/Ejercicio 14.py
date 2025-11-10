"""
14. Implemente un programa que permita introducir los valores A, B y C y realice el cálculo de
la expresión S. Muestre el resultado en pantalla.
• Si A / B > 30
S = (A / C) * B ^ 3
• Si A / B <= 30
S = 2 ^ 2 + 4 ^2 + 6 ^ 2 + … + 30 ^ 2

"""

def main():
    acumulador = 0

    a = int(input("Ingrese el valor A: "))
    b = int(input("Ingrese el valor B: "))
    c = int(input("Ingrese el valor C: "))

    if a / b > 30:
        s = (a / c) * (b ** 3)
        print("Fórmula usada: S = (A / C) * B³")
        print(f"S = {s}")
    else:
        print("Fórmula usada: S = 2² + 4² + 6² + … + 30²")
        for i in range(2, 31, 2):  
            acumulador += i ** 2
        print(f"S = {acumulador}")

main()
