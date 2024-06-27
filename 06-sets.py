### Sets ###
# A set is unordered collection of unique elements

my_set = set() # empty set
my_other_set = {} # empty dictionary

my_other_set = {"Daniel", "Gonzalez", 20} # if u introduce values, it will be a set instead of a dictionary
print(len(my_other_set)) # returns the number of elements in the set
print(my_other_set)
print("-------")

print("Daniel" in my_other_set) # validates if "Daniel" is in the set
my_other_set.add("Rodriguez") # adds a value to the set
my_other_set.remove("Rodriguez") # removes "Rodriguez" from the set
my_other_set.pop() # removes a random element from the set
my_other_set.clear() # removes all elements from the set

my_set = {"Daniel", "Gonzalez", 20} 
my_list = list(my_set) # converts the set to a list
print(my_list[0]) # and now im able to use the methods of list
print("-------")

my_other_set = {"Java", "Python", "C++"}
my_new_set = my_set.union(my_other_set) # returns a new set with the union of the two sets
print(my_new_set.union(my_new_set).union({"C#", "C"})) # returns a new set with the union of the two sets
print(my_new_set.difference(my_other_set)) # returns a new set with the difference between the two sets

del my_other_set # deletes the entire set, not the elements