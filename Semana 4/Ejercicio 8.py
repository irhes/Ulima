"""
8. Implemente un programa que permita calcular e imprimir la suma siguiente:
S = 50 + 48 + 46 + 44 + … + 20

"""

def main():
    suma = 0

    for i in range ( 50 , 19 , -2):

        suma = suma + i

    print(suma)

main()