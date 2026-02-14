class Animal:
    SPECIES = ""  # class variable

    def __init__(self):
        self.name = "Johnny"  # default value for he variable name from the class Animal
        self.age = 2

    def print_details(self):  # method, that displays the object state
        print(f"Name: {self.name}, age: {self.age}.")


snoopy = Animal()

# print(snoopy)
puppy = Animal()
dog = Animal()  # creates the second object of the Animal class

puppy.age = 1
puppy.name = "Rex Junior"
dog.age = 10
dog.name = "Rex Senior"
newline='\n'

print(f"puppy=({puppy}){newline}dog=({dog})")
print()
print(f"My dog: {puppy.name}, {puppy.age} and older dog: {dog.name}, {dog.age}")
