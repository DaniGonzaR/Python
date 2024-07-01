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
print("--------")

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
print("--------")

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
print("--------")

"""
Es numero primo?
Escribe un programa que compruebe si un numero es primo o no
Imprime los numeros primos entre 1 y 100
"""

def is_prime():

    for num in range(1, 101):
        if num >= 2:

            is_divisble = False

            for i in range(2, num):
                if num % i == 0:
                    is_divisble = True
                    break

            if not is_divisble:
                print(num)
    
is_prime()
print("--------")

"""
Programa que invierta el orden de un string
sin usar funciones propias del lenguaje
"""

def reverse_string(string):
    string_length = len(string)
    reversed_string = ""
    
    for i in range(0, string_length):
        reversed_string += string[string_length - i - 1]
    return reversed_string

print(reverse_string("Daniel"))