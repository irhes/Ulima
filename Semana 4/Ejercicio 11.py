"""
11. Implemente un programa que permita imprimir y contar los números múltiplos de 3 que hay
entre 1 y 100

"""
def main():
    contador = 0
    for i in range (1 , 101):
        if i % 3 == 0:
            print(i , end=" ")

            contador += 1

    print(f"\nHay {contador} multiplos de 3")

    
main()