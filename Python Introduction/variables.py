# A variable is a named location used to store data in the memory.
# It is helpful to think of variables as a container that holds data that can be changed later in the program

var = 10

# You can think of variables as a bag to store books in it and that book can be replaced at any time.

var = 15.5

# so, the value of number was 10. Later, it was changed to 15.5

# Assigning values to Variables in Python

# We use "="(assignment operator) to assign a value to a variable

str_var = "Hello, World!"
print(str_var)

# Python is a type-inferred language.
# So you don't have to explicitly define the variable type. It automatically knows that "Hello, World!" is a string and declares the website variable as a string.


# Again we can change value(ref) of the veriable "str_var"
# assigning a new value(ref) to "str_var"

str_var = "Hello, Earth!"

#Assigning multiple values to multiple variables

a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

# We also can assign same value to multiple variables at once,

x = y = z = "same"

print (x)
print (y)
print (z)

# Rules and Naming Convention for Variables and constants

"""
1. Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or
   an underscore (_).
   For example:
    snake_case
    MACRO_CASE
    camelCase
    CapWords

2. Create a name that makes sense. For example, "product" makes more sense than p.

3. If you want to create a variable name having two words, use underscore to separate them.
   For example:
    my_name
    current_salary

4. Use capital letters possible to declare a constant. For example:
    PI
    G
    MASS
    SPEED_OF_LIGHT
    TEMP

5. Never use special symbols like !, @, #, $, %, etc.

6. Don't start a variable name with a digit.
"""
