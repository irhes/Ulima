# -*- coding: utf-8 -*-
"""
4. Escribir un algoritmo en la que el usuario ingrese un subtotal y la tasa de gratuidad,
calcule la gratuidad, el total y lo muestre. Por ejemplo, si el usuario ingresa $10 como
subtotal y 15% para la tasa de gratuidad, el algoritmo muestre $1.5 como gratuidad
y $11.5 como total.

"""
def main():
    subtotal = float(input("Ingrese subtotal: "))
    tasa_de_gratuidad = float(input("Ingrese la tasa de gratuidad (%)"))

    gratuidad = subtotal * (tasa_de_gratuidad / 100)

    total = subtotal + gratuidad

    print("La gratuidad es $", gratuidad , "y" , "el total es $" , total)


main()

