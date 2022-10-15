"""The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal."""

# Syntax of for Loop

"""

for <var> in <iterable>:
    <statement(s)>

"""
# -----------------------------------------------------------
# Program to find the all the number that are divisible by 2 in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# iterate over the list
for val in numbers: #number is <iterable> and val is the <var>

    if val % 2 == 0: # <statement(s)>
        print(val)

# The out put is: 6 8 4 2 4

# ---------------------------------------------------------


# We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

#Syntax
""" range(start, stop, step) """

print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))

# Output

range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]

# -----------------------------------------------------------

# We can use the range() function in for loops to iterate through a sequence of numbers.

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

for i in range(10):
    print(i)

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])

#Output

"""
I like pop
I like rock
I like jazz
"""
# ----------------------------------------------------------------

# for loop with else
"""A for loop can have an optional else block as well.
    The else part is executed if the items in the sequence used in for loop exhausts."""

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# ----------------------------------------------------------------

# program to display student's marks from record

# this will help you with H.W
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')

# ---------------------------------------------------------------


