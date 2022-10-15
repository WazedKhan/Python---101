"""
Python dictionary is an ordered collection of items. Each item of a dictionary has a key/value pair.
Dictionaries are optimized to retrieve values when the key is known.

Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.
"""
# Defining a Dictionary
"""
dic = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
"""

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

# You can also construct a dictionary with the built-in dict() function. The argument to dict() should be a sequence of key-value pairs.

"""dic = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])"""

team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

# If the key values are simple strings, they can be specified as keyword arguments.
team2 = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

print(team)

print(team2)

# --------------------------------------------------------------------------------------------

# Accessing Dictionary Values

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error

# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])

# ---------------------------------------------------------------------------

# Changing and Adding Dictionary elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

# ----------------------------------------------------------------------------

# Removing elements from Dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)

# ---------------------------------------------------------

# Building a Dictionary Incrementally

person = {}

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
# ---------------------------------------------------------------------------------------

"""
Method	               Description
---------------------------------------------------------------------------------------------------------------------------------
clear()	            | Removes all items from the dictionary.

copy()	            | Returns a shallow copy of the dictionary.

fromkeys(seq[, v])	| Returns a new dictionary with keys from seq and value equal to v (defaults to None).

get(key[,d])	    | Returns the value of the key. If the key does not exist, returns d (defaults to None).

items()	            | Return a new object of the dictionary's items in (key, value) format.

keys()	            | Returns a new object of the dictionary's keys.

pop(key[,d])	    | Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.

popitem()	        | Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.

setdefault(key[,d])	| Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).

update([other])	    | Updates the dictionary with the key/value pairs from other, overwriting existing keys.

values()	        | Returns a new object of the dictionary's values
"""