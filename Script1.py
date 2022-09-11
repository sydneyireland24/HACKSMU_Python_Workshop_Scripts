''' The Purpose of this script is to teach the following concepts: '''
# How to write comments
# printing to the console
# variables
# arithmetic operators
# comparison operators
# logical operators
''' Did you notice I demonstrated two ways to do comments in Python? Wack '''

print("Print Statements")
print("***************************************************************************************************************")
''' Print Statements '''
print("Hello World!") # this is a print statement. As with other languages, you use these to display output to the console
print(1337) # you don't have to print just words, you can print numbers as well!
print(99, "bottles of beer on the wall") # you can combine multiple types of data into one print statement like so

print("====================================================")
# answers go here

''' Print Statements '''
print("***************************************************************************************************************")
print()

print("Variables")
print("***************************************************************************************************************")
''' Variables '''
# Remember in Java/C++/C/OOP language of choice how you need to declare a data type with variables?
# In python, that goes away!
test_integer = 7 # this is how to declare an integer
test_float = 6.9 # this is how to declare a float
test_bool = True # this is how to declare a boolean
test_bool2 = False # note how True and False have to be capitalized
test_string = "Sydney" # this is one way to declare a string
test_string2 = 'Gibbs' # this is another way to declare a string (can use either singe/double quotes)
# NOTE: there are no chars in Python - only strings with length one.

# you can print variables as well
print(test_integer)
print(test_float)
print(test_bool)
print(test_string)
print() # prints an empty line

# did you know you can check the type of a variable using the "type()" function?
print(type(test_integer))
print(type(test_float))
print(type(test_bool))
print(type(test_string))

print("====================================================")
# answers go here

''' Variables '''
print("***************************************************************************************************************")
print()

print("Arithmetic Operators")
print("***************************************************************************************************************")
''' Arithmetic Operators '''
# You can do a variety of arithmetic operations
print(7 + 5) # this is how to perform addition
print(3 - 9) # this is how to perform subtraction
print(2 * 5) # this is how to perform multiplication
print(4 % 3) # this is how to perform modulo
print(5**2) # this is how to perform the power function (5^2)

# division rules
print(10 / 5) # normal division (returns a float, even if result is whole number)
print(10 / 4) # normal division (returns a float)
print(10 // 4) # floor division (returns an int)

print("====================================================")
# answers go here


''' Arithmetic Operators '''
print("***************************************************************************************************************")
print()

print("Comparison Operators")
print("***************************************************************************************************************")
''' Comparison Operators '''
# Comparison operators are used to evaluate two values.
# After using them, they either yield false (0) or true (1)
print("Dog" > "dog") # should print false, "dog" does NOT come before "Dog" lexicographically
print(7 >= 7) # should print true, because 7 is equal to 7
print(1 + 1 == 3) # should print false, because 1 + 1 equals 2
print(1 + 1 != 3) # should print true, because 1+1 is NOT equal to 3
print(8.2*9.3 <= 9.2*9.3) # should print true, because the expression on the left is less than the one on the right
print("cat" < "catchphrase") # should print true, because cat comes before catchphrase lexicographically

print("====================================================")
# answers go here


''' Comparison Operators '''
print("***************************************************************************************************************")
print()

print("Logical Operators")
print("***************************************************************************************************************")
''' Logical Operators '''
# Logical Operators compare two or more logical statements, and determine whether the final result is True or False
# AND
# AND returns true when all the logical statements are also true (i.e. it returns true when every condition is true)
# Truth table for AND
# statement 1  | statement 2 | Result
# -----------------------------------
# True         | True        | True
# True         | False       | False
# False        | True        | False
# False        | False       | False

print(5 > 2 and 3 == 3) # should print True because all the statements are true
print("cat" == "dog" and "cat" == "cat") # should print false, because at least one statement is false

# OR
# OR returns true when AT LEAST ONE of the logical statements are also true (i.e. it only returns false when every
# condition is false)
# Truth table for OR
# statement 1  | statement 2 | Result
# -----------------------------------
# True         | True        | True
# True         | False       | True
# False        | True        | True
# False        | False       | False

val1 = 8.4
val2 = 2.0
print(6.9 == 7.2 or val1 > val2) # should print true, because at least one statement is true
print("computer science majors" == "studs" or "playing minecraft" == "touching grass") # should print false, since
# both statements are false

# NOT
# NOT returns the opposite of a logical statement
# Truth table for NOT
# statement 1  | Result
# ----------------------
# True         | False
# False        | True
print(not("SMU students" == "Humble People")) # the original statement is false, but with the not operator it's now true
print(not(1 + 1 == 3)) # the original statement is false, but with the not operator it's true

print("====================================================")
# answers go here

''' Logical Operators '''
print("***************************************************************************************************************")
print()
