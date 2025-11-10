"""
8. Realice un programa que permita a un usuario ingresar un determinado año. Deberá
imprimirse por pantalla si dicho año es bisiesto o no.
Observación: Para saber si un año es bisiesto se divide entre 4, si la división es exacta
entonces es bisiesto. Sin embargo, hay que tener cuidado con esta regla, ya que si el
año también es divisible entre 100 ya no será bisiesto. La excepción a la regla anterior
se da cuando el año es divisible entre 400.

"""

def main():
    año_bi = int(input("Ingrese cualquier año: "))

    if año_bi % 4 == 0:
        # Si es divisible entre 4, podría ser bisiesto
        if año_bi % 100 == 0:
            # Si también es divisible entre 100, podría no ser bisiesto
            if año_bi % 400 == 0:
                print(f"El año {año_bi} es bisiesto.")
            else:
                print(f"El año {año_bi} no es bisiesto.")
        else:
            # Divisible entre 4 pero no entre 100
            print(f"El año {año_bi} es bisiesto.")
    else:
        # No divisible entre 4
        print(f"El año {año_bi} no es bisiesto.")

main()
