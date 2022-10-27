"""
Creating a Function
In Python a function is defined using the def keyword:

"""


def avarage(*args):
    return sum(args) // len(args)

# a = 10
# b = 20


print(avarage(10, 20, 20, 30))