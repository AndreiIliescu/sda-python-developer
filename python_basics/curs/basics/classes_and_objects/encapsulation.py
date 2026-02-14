class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter
    def age(self):
        del self.__age


my_dog = Animal("Laica", 5)

my_dog.age = 3
print(my_dog.age)
print(my_dog.name)
my_dog.age = 0
# del my_dog.age
# print(my_dog.age)
