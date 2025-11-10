"""
7. Implemente un programa que permita calcular e imprimir el producto siguiente:
P = (1*2*3*4*5*…*20)

"""

def main():
    multiplicacion = 1

    for i in range (1 , 21):
        multiplicacion = multiplicacion * i

    print(multiplicacion)

main()