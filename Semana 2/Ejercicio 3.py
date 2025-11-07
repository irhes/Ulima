
"""
3. Escribir un algoritmo que lea el radio y la longitud del cilindro y calcule el área y
volumen usando las siguientes fórmulas, 

sabiendo que pi es 3.14159

área = radio * radio * pi
volumen = área * longitud

"""

def main():
    pi = 3.14159

    radio = float(input("Ingrese el radio del cilidro: "))
    longitud = float(input("Ingrese la longitud del cilindro: "))

    area = radio * radio * pi
    volumen = area * longitud
    
    print("El área del cilindro es", area , "y" , "el volumen del cilindro es" , volumen)
    
main()

