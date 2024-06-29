### Lists ###

my_list = list()
my_other_list = []

my_list = [20, 24, 62, 52, 30, 17]
print(my_list)
print(len(my_list))
print("----")

my_other_list = [20, 1.81, "Daniel", "Gonzalez"]
print(type(my_other_list))
print("----")

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count(20)) # counts the number of times 20 appears in the list
print("----")

age, height, address, surname = my_other_list
print(address)
print("----")

# Lists are mutable
print(my_other_list + my_other_list)
my_other_list.append(20) # adds 20 to the end of the list
my_other_list.insert(0, "Hello Guys") # adds "Hello Guys" to position 0 of the list
my_other_list[1] = "Blue" # replaces the element at position 1 with "Blue"
my_other_list.remove(20) # removes 20 from the list
my_other_list.pop() # removes the last element of the list
my_pop_element = my_other_list.pop(2) # removes the last element of the list and stores it in
my_other_list.clear() # removes all the elements of the list
del my_list[2] # removes the element at position 2 of the list
print(my_pop_element)
print(my_other_list)

my_new_list = my_other_list.copy() # creates a copy of the list
my_new_list.reverse # reverses the list
my_new_list.sort() # sorts the list in ascending order
print(my_new_list)

print(my_other_list[1:3]) # prints the elements from position 1 to position 3