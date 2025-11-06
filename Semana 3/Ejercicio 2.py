"""
Escriba un programa que solicite dos números enteros y calcule su división, 
mostrando si la división es exacta o no. Debe tener en cuenta que no se 
puede dividir entre cero.

"""
def main():

    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))

    if b == 0:
        print("No se puede dividir entre 0")
    else:
        print("El resultado es:", a / b)
        
main()
