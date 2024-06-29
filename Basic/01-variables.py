# Variables

# String
my_string_variable = "My String variable"
print(my_string_variable)
print("-------")

# Float
my_float_variable = 5.5
print(my_float_variable)
print("-------")

# Complex
my_complex_variable = 5 + 5j
print(my_complex_variable)
print("-------")

# Int
my_int_variable = 5
print(my_int_variable)
print("-------")

# Int to String
my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))
print("-------")

# Boolean 
my_boolean_variable = False
print(my_boolean_variable)
print("-------")

# All together
print(my_string_variable, my_int_variable, my_boolean_variable)
print("This is the value of:", my_boolean_variable)
print("-------")

# Length of the string variable
print(len(my_string_variable))
print("-------")

# One line variable
name, surname, alias, int = "Dani", "Gonzalez", "Gonza", 20
print(name, surname, alias, int)
print("-------")

# Input
name = input("What is your name? ")
surname = input("What is your surname? ")
age = input("What is your age? ")
print(name)
print(surname)
print(age)
print("-------")

# "Force" type of variable
address: str = "My address"
address = 32
print(type(address))
print(address)