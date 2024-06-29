### Modules ###
#import my_module
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 5, 5) # Calling the function from the module
sumValue(5, 5, 5) # Calling the function from the module
printValue(5) # Calling the function from the module
print("-----")

from math import pi as PI_VALUE # Importing a specific value from the module and renaming it
print(PI_VALUE)