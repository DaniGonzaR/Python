### Classes ###

class EmptyPerson: # Person class
    pass # Empty class

class Person:
    def __init__(self, name, surname): # Constructor
        self.name = name # Like this.name = name in Java (private property)
        self.surname = surname # Like this.surname = surname in Java (private property)

    def get_name(self): # Getter
        return self.name

    def walk(self): # Function
        print(f"{self.name} {self.surname} is walking")

my_person = Person("Daniel", "Gonzalez")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()

my_other_person = Person("Daniel", "Gonzalez")
my_other_person.name = "David"
print(f"{my_other_person.name} {my_other_person.surname}")