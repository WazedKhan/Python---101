"""
def <function_name>([<parameters>]):
    <statement(s)>

"""

"""
Component	     Meaning
def:     	     The keyword that informs Python that a function is being defined
<function_name>: A valid Python identifier that names the function
<parameters>:	 An optional, comma-separated list of parameters that may be passed to the function
:	Punctuation that denotes the end of the Python function header (the name and parameter list)
"""
# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")

# Calling a Function

my_function()

# Arguments

# Default Parameters

"""
def func(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')
"""

# Mutable Default Parameter Values

"""
def func(my_list=[]):
    my_list.append('###')
    return my_list
"""

