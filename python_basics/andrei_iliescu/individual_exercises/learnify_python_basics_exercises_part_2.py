'''PART 2'''
'''PYTHON CODE REFACTORING INTRODUCTION EXERCISES'''
# TODO 1: Create a Person class
#  ◦ add fields: name, surname, gender, age, personal ID number
#  ◦ add a method to check whether a person has reached the retirement age
#  (for women take retirement age >= 60, for men >= 65)
#  ◦ add a method that returns the age difference between a given person and another person:
#  ◦ make the method accept a Person type parameter
#  ◦ It should not return negative values as the difference of years.
#  ◦ Add a method that calculates and returns the number of years remaining to the retirement.

class Person:
    def __init__(self, name, surname, gender, age, id_number):
        self.name = name
        self.surname = surname
        self.gender = gender.lower()
        self.age = age
        self.id_number = id_number

    def is_able_to_retire(self):
        if self.gender == "woman" and self.age >= 60:
            return "She can retie"
        elif self.gender == "man" and self.age >= 65:
            return "He can retie"
        return "No can't retie"

    def age_difference(self, other_person):
        if not isinstance(other_person, Person):
            return None
        return abs(self.age - other_person.age)

    def years_until_retirement(self):
        if self.gender == "woman":
            if self.age < 60:
                return 60 - self.age
            else:
                return 0
        elif self.gender == "man":
            if self.age < 65:
                return 65 - self.age
            else:
                return 0
        return None


person1 = Person("Andreea", "Ionescu", "woman", 39, 50631)
person2 = Person("Andrei", "Iliescu", "man", 64, 98461)

print(f"{person1.name} can retire: {person1.is_able_to_retire()}")
print(f"{person2.name} can retire: {person2.is_able_to_retire()}")

print(f"Years until {person1.name}'s retirement: {person1.years_until_retirement()}")
print(f"Years until {person2.name}'s retirement: {person2.years_until_retirement()}")

print(f"Age difference between {person1.name} and {person2.name}: {person1.age_difference(person2)} years")
