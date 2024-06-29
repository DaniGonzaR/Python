### Functions ###

def my_function(): # Function definition
    print("This is a function")

my_function() # Function call

def sum_two_numbers(num1: int, num2: int): # INT to specify the type of the parameters to the programmer
    print(num1 + num2)

sum_two_numbers(5, 5) # Integer addition
sum_two_numbers("5", "5") # String concatenation
print("-----------")

def sum_two_numbers_with_return(num1: int, num2: int): # INT to specify the type of the parameters to the programmer
    return num1 + num2

my_result = sum_two_numbers_with_return(5, 5) # Storing the function result in a variable
print(my_result)
print("-----------")

def print_my_name(name: str, surname: str):
    print(f"{name} {surname}") # Formatting the string

print_my_name("Daniel", "Gonzalez")
print("-----------")

def print_my_name_with_default(name: str, surname: str, alias: str = "Without alias"): # Alias is the default value of the parameter
    print(f"{name} {surname} {alias}") # Formatting the string

print_my_name_with_default("Daniel", "Gonzalez")
print_my_name_with_default("Daniel", "Gonzalez", "Dani")
print("-----------")

def print_texts(*text): # *text allow ANY number of parameters
    print(text)

print_texts("Hey", "How", "Are", "You")