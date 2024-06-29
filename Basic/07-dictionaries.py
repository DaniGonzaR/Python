### Dictionaries ###

my_dict = dict()
my_other_dict = {}

my_other_dict = {"name": "Daniel", "lastname": "Gonzalez", "age": 20, 1: "Python"}
my_dict = {
            "name": "Daniel",
            "lastname": "Gonzalez",
            "age": 20,
            "Languages": {"Python", "Java", "C++"}
}

print(my_other_dict)
print(my_dict)
print(my_dict["name"]) # returns the value of the key "name"
print("-------")

del my_dict["age"] # deletes the key "age"
print("name" in my_dict) # validates if "Daniel" is in the dictionary (as a key not a value)
print("-------")

my_new_dict = my_dict.fromkeys(("Nombre", 1, "Country")) # returns a new dictionary with the keys from the first dictionary
print(my_new_dict)
print(my_dict.items()) # returns the items of the dictionary
print(my_dict.keys()) # returns the keys of the dictionary
print(my_dict.values()) # returns the values of the dictionary
