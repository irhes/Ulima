"""
6. Las dos raíces de la ecuación cuadrática “𝑎𝑥² + 𝑏𝑥 + 𝑐 = 0” pueden ser obtenidas
usando la siguiente formula:
# Fórmulas de las raíces cuadráticas:
#            __________
# r1 = -b + √(b² - 4ac)
#       ------------
#            2a
#
#            __________
# r2 = -b - √(b² - 4ac)
#       ------------
#            2a

La expresión “(b² − 4𝑎𝑐)” es llamada discriminante de la ecuación cuadrática:

- Si es positiva, la ecuación tiene 2 raíces reales
- Si es “0”, la ecuación tiene una raíz
- Si es negativo, la ecuación no tiene raíces reales.
Escriba un programa donde el usuario ingrese los valores de “a”, “b” y “c” y muestre el
resultado de la discriminante:

- Si el discriminante es positivo, debe mostrar las 2 raíces
- Si el discriminante es cero, debe mostrar la raíz.
- De otro modo, muestre el mensaje: “La ecuación no tiene raíces reales

"""
def main():

    a = int(input("Ingrese el número a :"))
    b = int(input("Ingrese el número b :"))
    c = int(input("Ingrese el número c :"))

    discriminante = b**2 - 4*a*c
    r1 = (-b + (discriminante)**(1/2)) / (2*a)
    r2 = (-b - (discriminante)**(1/2)) / (2*a)

    if discriminante > 0:
        print(f"Las raíces son: {r1} y {r2}")
    elif discriminante == 0:
        r = -b / (2*a)
        print(f"La raíz es: {r} ")
    else:
        print("La ecuación no tiene raíces reales")

main()