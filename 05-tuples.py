### Tuples ###

my_tuple = tuple() # empty tuple
my_other_tuple = () # empty tuple

my_tuple = (20, 1.81, "Daniel", "Gonzalez")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count(20)) # returns the number of times the value appears in the tuple
print(my_tuple.index("Gonzalez")) # returns the index of "Gonzalez" in the tuple
print(my_tuple[2:4]) # returns the tuple from index 3 to index 5
print("---------")

my_sum_tuples = my_tuple + my_tuple 
print(my_sum_tuples)
print("---------")

# del my_tuple # deletes the entire tuple