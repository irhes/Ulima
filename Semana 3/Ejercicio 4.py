"""
4. Escriba un programa que solicite el año actual y un valor de año cualquiera. El programa
debe mostrar cuántos años han pasado desde el año ingresado o cuántos años faltan
para llegar a ese año. En caso el año ingresado sea igual que el año actual, muestre un
mensaje indicando ello.

"""
def main():
    a = int(input("Ingrese el año actual: "))
    b = int(input("Ingrese cualquier año: "))

    if b < 0:
        print("No existen años negativos")
    else:
        if a > b:
            print(f"Han pasado {a - b} años desde el año {b}")
        elif a < b:
            print(f"Faltan {b - a} años para llegar al año {b}")
        else:
            print("Los años son iguales")

main()