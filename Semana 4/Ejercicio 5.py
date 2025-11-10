"""
5. Implemente un programa que permita calcular e imprimir la suma: 1+2+3+4+5+…+50

"""
def main():
    suma = 0 
    for numero in range (1 , 51):
        suma = suma + numero

    print(f"La suma de los numeros es {suma}")

main()