# OOP is a method of structuring a program by bundling related properties and behaviors into individual objects

# Conceptually, objects are like the components of a system. Think of a program as a factory assembly line of sorts.
# At each step of the assembly line a system component processes some material,
# ultimately transforming raw material into a finished product.

"""
Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars,
as well as relations between things, like companies and employees, students and teachers, and so on.
OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.
"""

# Define a Class in Python

"""
A class is a blueprint for how something should be defined. It doesn’t actually contain any data.
The Dog class specifies that a name and an age are necessary for defining a dog,
but it doesn’t contain the name or age of any specific dog.
"""

"""an instance is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore.
It’s an actual dog with a name, like Miles, who’s four years old.
"""

# An example of a Dog class:

class Dog:
    pass


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
In the body of .__init__(), there are two statements using the self variable:
self.name = name creates an attribute called name and assigns to it the value of the name parameter.
self.age = age creates an attribute called age and assigns to it the value of the age parameter.
"""

# Attributes created in .__init__() are called instance attributes.

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class attributes are attributes that have the same value for all class instances.

# --------------------------------------------------------------------------------------------


# Instantiate an Object in Python
class Dog:
    pass

a = Dog() #Creating a new object from a class is called instantiating an object.

print(a)

