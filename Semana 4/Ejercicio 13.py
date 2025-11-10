"""
13. Implemente un programa que permita introducir dos valores A y B y realice el cálculo de la
expresión S. Muestre el resultado en pantalla.
• Si A >= B
    S = 10 + 14 + 18 + … + 50
• Si (A / B) <= 30
    S = A ^ 2 + B ^ 2

"""

def main():
    acumulador = 0

    a = int(input("Ingrese el valor A: "))
    b = int(input("Ingrese el valor B: "))

    if a >= b:
        for i in range(10 , 51 , 4):
            acumulador += i
        print(acumulador, end=" ")
    
    elif ( a / b) <=30:
        s = (a ** 2) + (b ** 2)
        print(f"{s}")

main()