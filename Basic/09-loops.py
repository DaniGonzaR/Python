### Loops ###

# While loop

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Optional
    print("My condition is greater than 10")

print("While loop finished")

print("-----------")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("My condition is 15")
        break # Stops the loop
    
    print(my_condition)

print("-----------")

# For loop

my_list = [35, 24, 62, 62, 30, 30, 17]

for element in my_list:
    print(element)
else:
    print("My list has finished")

print("-----------")