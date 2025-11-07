
"""
5. La aceleración promedio está definida como el cambio de velocidad dividido entre el
tiempo para hacer ese cambio como se muestra en la siguiente formula:
A = (VF-VI) / T
Escriba un algoritmo en la que el usuario ingrese la velocidad inicial (VI) en
metros/segundo, la velocidad final (VF) en metros/segundo, el tiempo en segundos (T)
y muestre la aceleración promedio (A).

"""
def main():
    
    vi = float(input("Ingrese la velocidad inicial (m/s) : "))
    vf = float(input("Ingrese la velocidad final (m/s): "))
    t = float(input("Ingrese el tiempo (s): "))

    aceleracion_promedio = (vf-vi) / t
    
    print("La aceleración promedio es:" , aceleracion_promedio )

main()

