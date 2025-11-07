"""
5. Escriba un programa solicite pida tres números y que muestre un mensaje indicando si
los tres son iguales, si hay dos iguales o si son los tres distintos. Los mensajes serían:
“Ha escrito tres veces el mismo número”, “Ha escrito un número dos veces”, “Los tres
números son distintos” respectivament

"""
def main():
    a = int(input("Ingrese el número A :"))
    b = int(input("Ingrese el número B :"))
    c = int(input("Ingrese el número C :"))

    if a == b and b == c:
        print("Ha escrito tres veces el mismo número")
    
    elif a == b or b == c or c == a:
        print("Ha escrito un número dos veces")
    else:
        print("Los tres números son distintos")


main()


