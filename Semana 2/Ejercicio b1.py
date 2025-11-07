# -*- coding: utf-8 -*-
"""
1. Supongamos que usted ahorra $100 cada mes y lo deposita a una cuenta de ahorros
con una tasa efectiva anual de 5%. Por lo tanto, el interés efectivo mensual es:
    
TEM = ((1 + TEA)^(1/12)) − 1.
TEM = ((1 + 0.05)^(1/12)) – 1 = 0.004074

Después del primer mes el valor de su cuenta se convierte en:
100*(1+0.004074) = 100.4074

Después del Segundo mes, el valor de su cuenta es:
(100 + 100.4074) * (1 + 0.004074) = 201.2238597

Después del tercer mes, el valor de su cuenta es:
(100 + 201.2238597) * (1 + 0.004074) = 302.4510457}

Escriba un algoritmo donde el usuario ingrese el monto mensual que ahorra y muestre
el valor de su cuenta después del 4to mes.

"""
def main ():

    a = float(input("Ingrese el monto mensual: "))

    enero = a * (1 + 0.004074)

    febrero = ( a + enero) * (1 + 0.004074)

    marzo = (a + febrero) * (1 + 0.004074)

    abril = (a + marzo) * (1 + 0.004074)

    print("El valor de su cuenta en abril es:" , abril)
    
main()



