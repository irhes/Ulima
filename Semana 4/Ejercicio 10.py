"""
Implemente un programa que imprima los números del 1 al 100 y calcule la suma de todos
los númeos para por un lado (suma par) y por otro lado la de los impares (suma impar).
r
"""

def main():
    suma_par = 0
    suma_impar = 0

    for i in range(1, 101):
        print(i, end=" ")

        if i % 2 == 0:
            suma_par += i
        else:
            suma_impar += i
    print("\n")
    print(f"La suma de los números pares es: {suma_par}")
    print(f"La suma de los números impares es: {suma_impar}")

main()