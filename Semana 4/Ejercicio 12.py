"""
12. Implemente un programa que determine el conjunto de números que hay entre la unidad y
un determinado número introducido por el teclado. Tomando en cuenta el grupo de
números mencionado, su programa debe imprimir, sumar y contar los números del grupo
que son a la vez múltiplos de 2 y de 3.

"""

def main():
    n = int(input("Ingrese un número: "))

    suma = 0
    contador = 0

    print(f"\nNúmeros entre 1 y {n}:")
    for i in range(1, n + 1):
        print(i, end=" ")

    print(f"\n\nNúmeros múltiplos de 2 y 3 a la vez:")
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            print(i, end=" ")
            contador += 1
            suma += i

    print(f"\n\nCantidad de múltiplos de 2 y 3: {contador}")
    print(f"Suma de múltiplos de 2 y 3: {suma}")

main()
