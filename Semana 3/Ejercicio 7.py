"""
7. Un banco ofrece distintas tasas de interés a sus clientes dependiendo de los ahorros que
estos tengan. El banco pagará:
- El 4% si es que el depósito es de 1000 a más
- El 5% si es que el depósito llega hasta 5000
- El 8% si el depósito es de más de 5000
Desarrolle un programa que calcule cuánto se deberá pagar por interés dependiendo del
monto depositado.

"""
def main():
    ahorros = float(input("Ingrese su ahorro: "))

    if ahorros < 1000:
        print("No aplica tasa de interés.")

    elif 1000 <= ahorros < 5000:
        print("Se le pagará un interés del 4%: ", ahorros * (4/100))

    elif ahorros == 5000:
        print("Se le pagará un interés del 5%: ", ahorros * (5/100))
        #el enunciado dice si llega hasta 5000, en el anterior de 1000 a mas, por eso lo tome asi

    else:  
        print("Se le pagará un interés del 8%: ", ahorros * (8/100))

main()
