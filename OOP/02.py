class Dog:
    """
    A Dog class with a class attribute called .species and two instance attributes called .name and .age
    """
    species = "Canis familiaris"

    def __init__(self, name, age):
        # print(self)
        self.name = name
        self.age = age

# To instantiate objects of this Dog class, you need to provide values for the name and age.

snowy = Dog("Snowy", 5)
spike = Dog("Spike", 6)

print(snowy.name)
print(snowy.species)