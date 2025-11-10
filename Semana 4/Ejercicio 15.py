"""
15. Implemente un programa que permita imprimir en pantalla el siguiente patrón tomando
como entrada un valor “n” que determina la cantidad de líneas que se imprimirán (el
ejemplo muestra lo que debe mostrarse para para n = 3 → 3 líneas):

***
*****
*********

"""
def main():
    n = int(input("Ingrese la cantidad de líneas: "))

    for i in range(1, n + 1):
        print("*" * (2 * i + 1))

main()
