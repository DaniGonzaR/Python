### Conditionals ###

my_condition = False

if my_condition:
    print("The first IF is true")

my_condition = 5 * 2

if my_condition > 10 and my_condition < 20:
    print("greater than 10 and less than 20")
else: # else doesnt need a condition
    print("lesser than 10 or greater or equal than 20")

if my_condition > 10 and my_condition < 20:
    print("greater than 10 and less than 20")
elif my_condition == 10: # elif needs a condition
    print("equal to 10")

my_string = "My string"

if my_string:
    print("The string is not empty")

if not my_string:
    print("The string is empty")

if my_string == "My string":
    print("The strings are equal")