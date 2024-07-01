### Challenges ###

"""
FIZZ BUZZ
Escribe un programa que imprima los números del 1 al 100 ambos incluidos
con salto de linea en cada impresion sustituyendo los 
multiplos de 3 por FIZZ
multiplos de 5 por buzz
multiplos de 3 y 5 por FIZZ BUZZ.
"""

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZ BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)

fizz_buzz()

"""
Es un anagrama?
Funcion que reciba dos strings y devuelva True si son anagramas y False si no lo son.
Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra.
No hay que comprobar que ambas palabras existan
Dos palabras exactamente iguales no son anagramas.
"""

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("python", "typhon"))

"""
Fibonacci
Escribe un programa que imprima los primeros 50 numeros de la sucesion empezando en 0
La serie Fibonacci se compone de una sucesion de numeros donde cada numero es la suma de los dos anteriores
"""

def fibonacci():
    a, b = 0, 1
    for i in range(0, 51):
        print(a)
        a, b = b, a + b # a = b, b = a + b 

fibonacci()
