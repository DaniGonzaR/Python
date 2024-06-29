### Strings ###

# Formatting
name, surname, age = "Dani", "Gonzalez", 20
print("My name is {} {} and I am {} years old".format(name, surname, age))
print("My name is %s %s and I am %d years old" % (name, surname, age))
print("--------")

# Character depacking
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)
print("--------")

# Slicing
language_slice = language[1:3]
print(language_slice)
print("--------")

# Reversing
language_reverse = language[::-1]
print(language_reverse)
print("--------")

# Functions
print(language.upper()) # Uppercase
print(language.lower()) # Lowercase
print(language.capitalize()) # Capitalize the first letter

print(language.count("t")) # Count the number of times a character appears in a string
print(language.find("t")) # Find the position of a character in a string
print(language.replace("t", "T")) # Replace a character in a string

print(language.isnumeric()) # Check if a string is numeric
print("--------")