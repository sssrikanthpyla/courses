
# Keywords in Python
# Keywords are the reserved words in Python.
# We cannot use a keyword as a variable name, function name or any other identifier.
# Keywords are case sensitive.


# List of Keywords in Python
# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield

# Example
# Keywords in Python
import keyword
print(keyword.kwlist)
# Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# You cannot use these keywords as variable names, function names, or any other identifiers.
# Example
# You will get an error if you use a keyword as a variable name:
# False = "Srikanth"
# print(False) # Output: SyntaxError: can't assign to keyword
