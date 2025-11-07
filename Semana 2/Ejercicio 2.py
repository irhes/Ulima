
"""
2. Escribir un algoritmo que convierta libras a kilogramos. El usuario ingresa el número
de libras, lo convierta a kilogramos y se muestra el resultado. Una libra es 0.4536
kilogramos

"""
def main():
    
    libras = float(input("Ingrese el peso en libras: "))

    kilos = 0.4536 * libras

    print("El peso en kilos es: " , kilos)
    
main()
