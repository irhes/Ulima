"""

1. Escribir un algoritmo que lea una longitud medida en pies y la convierta en metros y
muestre el resultado. (Un pie es 0.3048 metros)

"""
def main():

    pies = float(input("Ingrese la longitud en pies: "))

    metros = 0.3048 * pies

    print("La longitud en metros es: ", metros)
    
main()
