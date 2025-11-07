# -*- coding: utf-8 -*-
"""
7.- Escribir un algoritmo que determine el área (pi * radio * radio) y perímetro (2 * pi
* r) de la circunferencia. Se tiene que ingresar todos los datos necesarios y mostrar
el resultado.

"""
def main():
    
    a = float(input("Ingrese el radio de la circunferencia: "))
    pi = 3.1416
    
    area = pi * a * a
    perimetro = 2 * pi * a
    
    print("El área y el perímetro de la circunferencia son respectivamente:" 
          , area , "y" , perimetro)
    
main()






