# Data type:-
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# Getting the Data Type
# You can get the data type of any object by using the type() function:
# Example
x = 5
print(type(x)) # Output: <class 'int'>


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# Example
x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name" : "John", "age" : 36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
# Example
x = str("Hello World") # str
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex
x = list(("apple", "banana", "cherry")) # list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(5) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview


# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
# Example
print("Hello")
print('Hello')


# Numbers
# There are three numeric types in Python:
# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:
# Example
x = 1 # int
y = 2.8 # float
z = 1j # complex
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'complex'>

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Example
x = 1
y = 35656222554887711
z = -3255522
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'int'>
print(type(z)) # Output: <class 'int'>

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Example
x = 1.10
y = 1.0
z = -35.59
print(type(x)) # Output: <class 'float'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'float'>
# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example
x = 35e3
y = 12E4
z = -87.7e100
print(type(x)) # Output: <class 'float'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'float'>

# Complex
# Complex numbers are written with a "j" as the imaginary part:
# Example
x = 3+5j
y = 5j
z = -5j
print(type(x)) # Output: <class 'complex'>
print(type(y)) # Output: <class 'complex'>


# Boolean
# Booleans represent one of two values: True or False.
# Example
x = True
y = False
print(type(x)) # Output: <class 'bool'>
print(type(y)) # Output: <class 'bool'>
# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
# Example
print(10 > 9) # Output: True
print(10 == 9) # Output: False
print(10 < 9) # Output: False
# When you run a condition in an if statement, Python returns True or False:
# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return:
# Example
print(bool("Hello")) # Output: True
print(bool(15)) # Output: True
# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# Example
bool("abc") # Output: True
bool(123) # Output: True
bool(["apple", "cherry", "banana"]) # Output: True
# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# Example
bool(False) # Output: False
bool(None) # Output: False
bool(0) # Output: False
bool("") # Output: False
bool(()) # Output: False
bool([]) # Output: False
bool({}) # Output: False
# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
# Example
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) # Output: False
# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:
# Example
def myFunction() :
  return True
print(myFunction()) # Output: True


# Lists
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
# Example
thislist = ["apple", "banana", "cherry"]
print(thislist)
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
# Example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# List Length
# To determine how many items a list has, use the len() function:
# Example
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# List Items - Data Types
# List items can be of any data type:
# Example
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates
# Since tuple are indexed, tuples can have items with the same value:
# Example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Tuple Length
# To determine how many items a tuple has, use the len() function:
# Example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# Tuple Items - Data Types
# Tuple items can be of any data type:
# Example
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
# A tuple can contain different data types:
# Example
tuple1 = ("abc", 34, True)
print(tuple1)
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Example
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# Example
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed
# Sets cannot have two items with the same value.
# Example
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Set Length
# To determine how many items a set has, use the len() method.
# Example
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Set Items - Data Types
# Set items can be of any data type:
# Example
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
# A set can contain different data types:
# Example
set1 = {"abc", 34, True}
print(set1)
# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Example
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Ordered
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Allow Duplicates
# Since dictionaries are indexed, dictionaries can have items with the same value:
# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
# Dictionary Items - Data Types
# Dictionary items can be of any data type:
# Example
dict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(dict1)
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Example
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
# Example
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


# Arrays
# Arrays are used to store multiple values in one single variable.
# Create an array containing car names:
# Example
cars = ["Ford", "Volvo", "BMW"]
# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
# The solution is an array!
# An array can hold many values under a single name, and you can access the values by referring to an index number.
# Access the Elements of an Array
# You refer to an array element by referring to the index number.
# Get the value of the first array item:
# Example
x = cars[0]
# Modify the value of the first array item:
# Example
cars[0] = "Toyota"
# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
# Return the number of elements in the cars array:
# Example
x = len(cars)
# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
# Example
for x in cars:
  print(x)
# Adding Array Elements
# You can use the append() method to add an element to an array.
# Add one more element to the cars array:
# Example
cars.append("Honda")
# Removing Array Elements
# You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array:
# Example
cars.pop(1)
# The del keyword also removes the specified index:
# Example
del cars[0]
# The del keyword can also delete the array completely:
# Example
del cars
# The clear() method empties the cars array:
# Example
# cars.clear()
# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.






