''' The Purpose of this script is to teach the following concepts: '''
# user input
# lists
# strings
# functions

print("User Input")
print("***************************************************************************************************************")
''' User Input '''
# suppose you want a user to imput information
# you can use the "input()" method to get input from the keyboard
# note: it always takes in input() as a string, so you'll have to convert input if you want an int or float

fName = input("Please enter your first name: ") # prints "please enter your first name" and stores input from keyboard
# into the fName variable

print("Your first name is: ", fName)

age = int(input("Please enter your age: "))

print("Your age is: ", age)

print("====================================================")
# write a statement that takes in a float from a user and prints it out
myFloat = float(input("Please enter a float: "))

''' User Input '''
print("***************************************************************************************************************")
print()

print("Strings")
print("***************************************************************************************************************")
''' Strings '''
str1 = "Hello World!"
str2 = "HACKSMU is here 4 u"
str3 = "abcdefghijklmnopqrstuvwxyz"

# getting the length of a string
# to get the length of a string, you use the len() method
print(len(str1)) # prints the length of str1
print(len(str2)) # prints the length of str2
print(len(str3)) # prints the length of str3

# indexing with []
# you can access specific characters within strings using brackets
# the first letter of the string is at index 0, the second is at index 1, etc.
# the last letter is at index len(string) - 1

print(str1[4]) # prints the 5th character of str1
print(str2[0]) # prints the 1st letter of str2
print(str3[len(str3) - 1]) # prints the last letter str3

# slicing with [x:y]
# you can get substrings within strings using brackets as well
print(str1[0:4]) # prints the first 4 letters of str1
print(str2[11:]) # get the entirety of str2 starting at position 11
print(str3[:3]) # gets the first 3 letters of str3

# in keyword
# checks if a substring is found within a string
print("hell" in str1) # should print False (case-sensitive)
print("here" in str2) # should print True
print("alphabet" in str3) # should print False

# upper() and lower()
# converts a string to all uppercase or all lowercase

print(str1.upper())
print(str2.lower())
print(str3.upper())

# you can also replace characters within strings
print(str1.replace('l', 'w'))
print(str2.replace('u', "owo"))

# lastly, you can also concatenate strings to form a new monstrosity
print(str1 + " Did you know that ", str2)

print("====================================================")

''' Strings '''
print("***************************************************************************************************************")
print()

print("Lists")
print("***************************************************************************************************************")
''' Lists '''

list1 = [1, 5, 10, 98, 76, 45]
list2 = ["C++", "Java", "Python", "SQL"]

# you can print lists and their entirety like so:
print(list1)
print(list2)

# like strings, you can get the length of a list with len()
print(len(list1))
print(len(list2))

# like strings, you can perform indexing on lists
print(list1[4]) # prints the 5th element from list1
print(list2[len(list2) - 1]) # prints the last element from list2

# like strings, you can get a range of items from a list with brackets as well
print(list1[1:4]) # prints the second to the fourth element of list1
print(list1[3:]) # prints the last 3 elements of list1
print(list2[:2]) # prints the first 2 elements of list2

# you can insert elements into a list
list1.insert(1, 333) # puts 333 as the second element of list1
print(list1)
list2.insert(2, "JavaScript") # puts JavaScript as the third element of list2
print(list2)

# you can also append elements to the end of a list
list1.append(789)
list2.append("COBOL")
print(list1)
print(list2)

# you can also sort 

list3 = list1 + list2
print(list3)

print("====================================================")

''' Lists '''
print("***************************************************************************************************************")
print()

print("Functions")
print("***************************************************************************************************************")
''' Functions '''

print("====================================================")

''' Functions '''
print("***************************************************************************************************************")
print()
