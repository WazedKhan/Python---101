# Instance Methods
# Instance methods are functions that are defined inside a class and can only be called from an instance of that class.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # This method returns the string representation of the object.
    def __str__(self):

        """This method is also used as a debugging tool when the members of a class need to be checked."""

        return f'{self.name}-> of Dog Class'

miles = Dog("Miles", 4)

print(miles)