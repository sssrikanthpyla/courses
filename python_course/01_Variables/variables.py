# Variable in Python:-
""" 
    Variables are containers for storing data values.
    Unlike other programming languages, Python has no command for declaring a variable.
    A variable is created the moment you first assign a value to it. 
"""
# Example
x = 5
y = "Srikanth"
print(x) # Output: 5
print(y) # Output: Srikanth


# Variables do not need to be declared with any particular type and can even change type after they have been set.
# Example
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x) # Output: Sally

# Casting in Python:- 
# If you want to specify the data type of a variable, this can be done with casting.
# Example
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0


# Get the Type
# You can get the data type of a variable with the type() function.
# Example
x = 5
y = "Srikanth"
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'str'>


# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:
# Example
x = "Srikanth"
# is the same as
x = 'Srikanth'


# Case-Sensitive
# Variable names are case-sensitive.
# Example
# This will create two variables:
a = 4
A = "Srikanth"
print(a) # Output: 4
print(A) # Output: Srikanth


# Python allows you to assign values to multiple variables in one line:
# Example
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Output: Orange
print(y) # Output: Banana
print(z) # Output: Cherry


# And you can assign the same value to multiple variables in one line:
# Example
x = y = z = "Orange"
print(x) # Output: Orange
print(y) # Output: Orange
print(z) # Output: Orange


# Output Variables :- The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
# Example
x = "awesome"
print("Python is " + x)


# You can also use the + character to add a variable to another variable:
# Example
x = "Python is "
y = "awesome"
z = x + y
print(z) # Output: Python is awesome


# For numbers, the + character works as a mathematical operator:
# Example
x = 5
y = 10
print(x + y) # Output: 15


# If you try to combine a string and a number, Python will give you an error:
# Example
x = 5
y = "Pyla"
# print(x + y) # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Global Variables
""" 
    Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    Global variables can be used by everyone, both inside of functions and outside. 
"""
# Example
# Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc() # Output: Python is awesome


""" 
    If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
    The global variable with the same name will remain as it was, global and with the original value.
"""
# Example
# Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc() # Output: Python is fantastic
print("Python is " + x) # Output: Python is awesome


# The global Keyword
"""
    Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
    To create a global variable inside a function, you can use the global keyword.
"""
# Example
# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) # Output: Python is fantastic


# Also, use the global keyword if you want to change a global variable inside a function.
# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) # Output: Python is fantastic

# Rules for Naming Variables
""" 
    A variable name must start with a letter or the underscore character.
    A variable name cannot start with a number.
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# Example
# Legal variable names:
myvar = "Srikanth"
my_var = "Srikanth"
_my_var = "Srikanth"
myVar = "Srikanth"
MYVAR = "Srikanth"
myvar2 = "Srikanth"

# Illegal variable names:
# 2myvar = "Srikanth"
# my-var = "Srikanth"
# my var = "Srikanth"


# Dynamic Typing
"""
    Python has dynamic typing, meaning you can reassign variables to different data types.
    This makes Python very flexible in assigning data types; it differs from other languages that are statically typed.
"""
# Example
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x) # Output: Sally


# Delete a Variable Using del Keyword
# You can delete a variable using the del keyword.
# Example
x = "Srikanth"
print(x) # Output: Srikanth

del x
# print(x) # Output: NameError: name 'x' is not defined





