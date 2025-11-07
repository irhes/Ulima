# -*- coding: utf-8 -*-
"""
4. La cantidad total de infectados (N) por el virus T1 en la ciudad K se encuentra dada
por la siguiente expresión:
N(t) = N0 * e^5t

Donde:
N0: Cantidad de personas infectadas al inicio.
e: Número de Euler. Aproxímelo a 2.72.
t: Cantidad de días desde el inicio de la infección.
Considerando que la infección se inició el día 1 de abril, reportándose 5 casos, se le
solicita implementar un algoritmo que permita determinar cuántos nuevos infectados
se reportarían el día 5 de abril.
Notas:
• Considere la existencia del operador “^” para cálculos de potencia.
Ejemplo:
a ← 3 ^ 2
En este caso, la variable “a” almacenará el valor de 32 = 9.
• Asuma que todavía no se reportan casos de personas curadas y que además
no se han producido fallecimientos durante el periodo de análisis.

"""
def main():
    
    N0 = 5
    e = 2.72
    t = 4
    Nt = N0 * (e** (5 *t))

    print("La cantidad de infectados el dia 5 de Abril es:" , Nt)

main()

