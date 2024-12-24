# Literals in Python
# Literals are data used for representing fixed values.
# They are called literals because their values literally represent themselves.
# In Python, literals are categorized into five classes:

# 1. Numeric Literals

# Numeric Literals are immutable (unchangeable).
# Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.
# Integers can be of any length, it is only limited by the memory available.
# A floating-point literal is a decimal number.
# A complex literal consists of an integer or a float followed by 'j' or 'J'.
# Example
# Integers
# Example
x = 1
y = 35656222554887711
z = -3255522
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'int'>
print(type(z)) # Output: <class 'int'>

# Floats
# Example
x = 1.10
y = 1.0
z = -35.59
print(type(x)) # Output: <class 'float'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'float'>

# Complex
# Example
x = 3+5j
y = 5j
z = -5j
print(type(x)) # Output: <class 'complex'>
print(type(y)) # Output: <class 'complex'>
print(type(z)) # Output: <class 'complex'>


# 2. String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
# Example
print("Hello")

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
# Example
a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# Example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Example
a = "Hello, World!"
print(a[1]) # Output: e

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example
b = "Hello, World!"
print(b[2:5]) # Output: llo

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
b = "Hello, World!"
print(b[-5:-2]) # Output: orl

# String Length
# To get the length of a string, use the len() function.
# Example
a = "Hello, World!"
print(len(a)) # Output: 13

# String Methods
# Python has a set of built-in methods that you can use on strings.
# Example
a = " Hello, World! "
print(a.strip()) # Output: Hello, World!

# The strip() method removes any whitespace from the beginning or the end:
# Example
a = " Hello, World! "
print(a.strip()) # Output: Hello, World!

# The lower() method returns the string in lower case:
# Example
a = "Hello, World!"
print(a.lower()) # Output: hello, world!

# The upper() method returns the string in upper case:
# Example
a = "Hello, World!"
print(a.upper()) # Output: HELLO, WORLD!

# The replace() method replaces a string with another string:
# Example
a = "Hello, World!"
print(a.replace("H", "J")) # Output: Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator:
# Example
a = "Hello, World!"
print(a.split(",")) # Output: ['Hello', ' World!']

# Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
# Example
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # Output: True

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Example
a = "Hello"
b = "World"
c = a + b
print(c) # Output: HelloWorld

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example
age = 36
txt = "My name is John, I am " + age
print(txt) # Output: TypeError: can only concatenate str (not "int") to str

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # Output: My name is John, and I am 36

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder = '''I want {0} pieces of item {1} for {2} dollars.'''
print(myorder.format(quantity, itemno, price)) # Output: I want 3 pieces of item 567 for 49.95 dollars.

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# Example
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # Output: We are the so-called "Vikings" from the north.

# Other escape characters used in Python:
# Code	Result
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
# Example
txt = "Hello\nWorld!"
print(txt) # Output: Hello
           #         World!


# 3. Boolean Literals
# Boolean literals are the two constant objects False and True.
# They are used to represent truth values (other values can also be considered false or true).
# In numeric contexts (for example, when used as the argument to an arithmetic operator), they behave like the integers 0 and 1, respectively.
# The built-in function bool() can be used to cast any value to a Boolean, if the value can be interpreted as a truth value:
# Example
print(bool("Hello")) # Output: True
print(bool(15)) # Output: True

# Example
x = "Hello"
y = 15
print(bool(x)) # Output: True
print(bool(y)) # Output: True

# Example
x = 0
print(bool(x)) # Output: False

# Example
x = None
print(bool(x)) # Output: False

# Example
x = ""
print(bool(x)) # Output: False

# Example
x = []
print(bool(x)) # Output: False

# Example
x = {}
print(bool(x)) # Output: False

# Example
x = ()
print(bool(x)) # Output: False

# Example
x = set()
print(bool(x)) # Output: False

# Example
x = 1
print(bool(x)) # Output: True

# Example
x = -1
print(bool(x)) # Output: True

# Example
x = 0.1
print(bool(x)) # Output: True

# Example
x = "Hello"
print(bool(x)) # Output: True

# Example
x = [1, 2, 3]
print(bool(x)) # Output: True

# Example
x = {1: "One", 2: "Two"}
print(bool(x)) # Output: True

# Example
x = (1, 2, 3)
print(bool(x)) # Output: True

# Example
x = {"One", "Two", "Three"}
print(bool(x)) # Output: True

# Example
x = True
print(bool(x)) # Output: True

# Example
x = False
print(bool(x)) # Output: False

# Example
x = 0
y = 15
print(bool(x)) # Output: False
print(bool(y)) # Output: True



# 4. Special Literals
# Python contains one special literal i.e. None.
# We use it to specify that the field has not been created.
# Example
x = None
print(x) # Output: None

# Example
x = None
y = 0
print(bool(x)) # Output: False
print(bool(y)) # Output: False



# 5. Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
# List literals are written within square brackets [].
# Tuple literals are written within parentheses ().
# Dict literals are written within curly brackets {}.
# Set literals are written within curly brackets {}.
# Example
# List
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Tuple
fruits = ("apple", "banana", "cherry")
print(fruits) # Output: ('apple', 'banana', 'cherry')

# Dict
fruits = {"name": "apple", "quantity": 2}
print(fruits) # Output: {'name': 'apple', 'quantity': 2}

# Set
fruits = {"apple", "banana", "cherry"}
print(fruits) # Output: {'apple', 'banana', 'cherry'}
# Note: A set is a collection which is both unordered and unindexed.
# Note: Sets are unordered, so the items will appear in a random order.
# Note: You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Example
fruits = {"apple", "banana", "cherry"}
for x in fruits:
    print(x) # Output: cherry
             #         banana
             #         apple
    
# Example
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits) # Output: True

# Example
fruits = {"apple", "banana", "cherry"}
print("orange" in fruits) # Output: False
# Note: Once a set is created, you cannot change its items, but you can add new items.
# Example
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) # Output: {'apple', 'banana', 'cherry', 'orange'}

# Example
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # Output: {'apple', 'cherry'}

# Example
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) # Output: {'apple', 'cherry'}

# Example
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) # Output: set()

# Example
fruits = {"apple", "banana", "cherry"}
del fruits
# print(fruits) # Output: NameError: name 'fruits' is not defined

# Example
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits) # Output: {'banana', 'cherry'}

# Example
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) # Output: set()

# Example
fruits = {"apple", "banana", "cherry"}

# Copy a set
x = fruits.copy()
print(x) # Output: {'apple', 'banana', 'cherry'}


# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Example
fruits = set(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits) # Output: {'apple', 'banana', 'cherry'}
# Note: The set() constructor can also be used to create an empty set.
# Example
fruits = set()
print(fruits) # Output: set()
# Note: Sets are unordered, so the items will appear in a random order.
# Note: You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Note: Once a set is created, you cannot change its items, but you can add new items.
# Note: To add one item to a set use the add() method.
# Note: To add more than one item to a set use the update() method.
# Note: To remove an item in a set, use the remove(), or the discard() method.
# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
# Note: You can also use the clear() method to empty the set.
# Note: The del keyword will delete the set completely.
# Note: It is also possible to use the set() constructor to make a set.


