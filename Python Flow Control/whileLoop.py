# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

# Syntax of while Loop in Python
"""
while test_expression:
    Body of while

"""

# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

# -------------------------------------------------
'''Example to illustrate the use of else statement with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")