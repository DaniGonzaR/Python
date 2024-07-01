"""
FIZZ BUZZ
Escribe un programa que imprima los números del 1 al 100 ambos incluidos
con salto de linea en cada impresion sustituyendo los 
multiplos de 3 por FIZZ
multiplos de 5 por buzz
multiplos de 3 y 5 por FIZZ BUZZ.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZ BUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)