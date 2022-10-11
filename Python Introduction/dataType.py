# Data types in Python:
"""
Every value in Python has a datatype. Since everything is an object in Python programming,
data types are actually classes and variables are instance (object) of these classes.
"""

#Python Numbers:
"""Integers(1,2,3), floating(1.5, 2.6) point numbers and complex(1+2i, 5-5j) numbers fall under Python numbers category.
They are defined as int, float and complex classes in Python."""

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
