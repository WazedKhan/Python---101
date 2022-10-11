
#Python List
"""Lists are used to store multiple items in a single variable.
   Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets
   Ex: [item, item, item ].
"""

# a list of programming languages
['Python', 'C++', 'JavaScript']

# list can have any data types
my_list = [1, "Hello", 3.4, True]

# A list can also have another list as an item. This is called a nested list.
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

#Access List Elements

# ------------------------------------------------------------------------------------------------

my_list = [1,2,3,4,5,6,7]

# first item
print(my_list[0])  #1

# third item
print(my_list[2])  # 3

# fifth item
print(my_list[4])  # 5

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])

# Negative indexing:
my_list = ['p','r','o','b','e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])

# List Slicing in Python
# List slicing in Python

my_list = ['t',' h', 'i', 's', 'p', 'y', 't', 'h', 'o', 'n']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
# ----------------------------------------------------------------------
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# -----------------------------------------------------------------------
# Delete List Elements
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
print(my_list)

# -----------------------------------------------------------------------

# Poping element from list

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

# -----------------------------------------------------------------------
# Python List Methods
"""
Methods	Descriptions
append()	adds an element to the end of the list
extend()	adds all elements of a list to another list
insert()	inserts an item at the defined index
remove()	removes an item from the list
pop()	returns and removes an element at the given index
clear()	removes all items from the list
index()	returns the index of the first matched item
count()	returns the count of the number of items passed as an argument
sort()	sort items in a list in ascending order
reverse()	reverse the order of items in the list
copy() 	returns a shallow copy of the list
"""