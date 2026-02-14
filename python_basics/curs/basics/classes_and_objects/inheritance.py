class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi from another world! My name is {self.name}")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def another_method(self):
        print(f"I am {self.age} years old.")

    def greet(self):
        print(f" Hello i am a child {self.name}")
        super().greet()


a = Child("Maria", 11)
b = Parent("Paul")

a.greet()
a.another_method()
b.greet()
