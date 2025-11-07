# -*- coding: utf-8 -*-
"""
3. El índice de masa corporal (IMC) es una medida que evalúa la salud en base al
peso. Puede ser calculada tomando el peso en kilogramos y dividirla entre el
cuadrado de la estatura en metros. Escriba un algoritmo que solicite al usuario
ingresar el peso en libras y la estatura en pulgadas y muestre el IMC. (Nota: 1 libra
equivale a 0.4536 kilogramos y una pulgada equivale a 0.0254 metros)

"""
def main():
    
    libras = float(input("Ingrese su peso en libras"))
    pulgadas = float(input("Ingrese su estatura en pulgadas"))

# parte 2
    kilos = libras * 0.4536
    metros = pulgadas * 0.0254
    
    IMC = kilos / (metros ** 2)
    
    print("El IMC:" , IMC)

main()

