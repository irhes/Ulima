"""
3. Escriba un programa que solicite dos números y muestre en pantalla cuál 
es el menor y cuál el mayor. En caso sean iguales debe mostrar un mensaje 
indicando ello.

"""
def main():

    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese un numero:"))

    if a < b:
        print(f"El número {a} es menor y el número {b} es mayor")
    elif a > b:
        print(f"El número {b} es menor y el número {a} es mayor")
    else:
        print("Los dos números son iguales")

main()