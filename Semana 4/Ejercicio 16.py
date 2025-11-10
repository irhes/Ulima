"""
16. Implemente un programa que lea desde el teclado una cadena de caracteres, un valor “n”
que representa el orden de una matriz y permita mostrar el siguiente patrón en pantalla (se
muestran resultados para n = 3 → matriz de 3 x 3).

Si n = 3

palabra = "hola"

hola hola hola
hola hola hola
hola hola hola

"""
def main():
    palabra = int(input("Ingrese el numero de la matriz: "))

    for i in range (1 , palabra + 1):
        print("hola   " * palabra )

main()


