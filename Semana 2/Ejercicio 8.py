# -*- coding: utf-8 -*-
"""
8.- Escribir un programa que lea la longitud de los catetos (a y b) de un triángulo
rectángulo en cm y calcule la longitud de la hipotenusa(c) en cm. Formula de
hipotenusa: c^2 = a^2 + b^2

"""
a = float(input("Ingrese el cateto a: "))
b = float(input("Ingrese el cateto b: "))

h = a**2 + b**2

h = h ** (1/2)

print("La hipotenusa es: " , h)







