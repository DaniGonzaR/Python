### Exception Handling ###

numberOne, numberTwo = 5, "2"

try: # Must
    print(numberOne + numberTwo)
except: # Must
    print("Something went wrong") # If there is an exception
else: # Optional
    print("Everything went fine") # If there is no exception
finally: # Optional
    print("The execution continues") # Always executed

print("-----------")

# Exception types

try:
    print(numberOne + numberTwo)
except TypeError:
    print("TypeError ocurred")
except ValueError:
    print("ValueError ocurred")

print("-----------")
# Exception info captured

try:
    print(numberOne + numberTwo)
except ValueError as error: # error = variable to store the exception info
    print(error)
except Exception as exception:
    print(exception)