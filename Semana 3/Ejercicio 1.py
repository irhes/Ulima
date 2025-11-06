""" 1. Escriba un programa que siga la siguiente regla de pago:
- Si gasto hasta $100, pago con dinero en efectivo
- Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito
- Si no, pago con tarjeta de crédito.
El programa debe leer el monto del pago y mostrar en pantalla el medio de pago que se
utilizará."""

def main():

    a = float(input("Ingrese el monto de pago: "))

    if a <= 100:
        print("Use dinero en efectivo")
    elif a < 300:
        print("Use tarjeta de debito")
    else:
        print("Use tarjeta de credito")

main()