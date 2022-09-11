import random

''' The Purpose of this script is to teach the following concepts: '''
# if-else statements and conditional statements
# while loops
# for loops + range() function
# indentation rules
# random numbers

print("If-Else Statements and Conditional Statements")
print("***************************************************************************************************************")
''' If-Else Statements and Conditional Statements '''
# Conditional Statements (i.e. if-else statements) are used when you have multiple paths you can take after an action,
# depending on the outcome of that action.

michael = "cool"
if michael == "cool":
    print("This statement will execute because it's true")
else:
    print("If michael is equal to anything else, this statement would execute")

# you can have multiple outcomes by using elif statements:
number_grade = 76
if number_grade >= 90:
    print("You got an A")
elif number_grade <= 89 and number_grade >= 80:
    print("You got a B")
elif number_grade <= 79 and number_grade >= 70:
    print("You got a C")
else:
    print("You got an F")

# NOTE ABOUT INDENTATIONS:
# you MUST have the code within if/elif/else statements indented FURTHER than the condition statement. Below is a
# commented out example of incorrect indentation, plus it wouldn't compile, also L + ratio
# if 700 == 700:
# print("L + ratio lol bozo")

print("====================================================")

# write if-else statements to check someone's is under 25, between 25 and 50, or above 50 years old based on their
# birth year
birth_year = 1997
if 2022 - birth_year < 25:
    print("Under 25")
elif 2022 - birth_year >= 25 and 2022 - birth_year <= 50:
    print("Between 25 and 50")
else:
    print("Above 50")

''' If-Else Statements and Conditional Statements '''
print("***************************************************************************************************************")
print()

print("While Loops")
print("***************************************************************************************************************")
''' While Loops '''

# let's say you have to complete an action, where you are unsure how many times it's going to occur.
# While loops allow you to execute code *while* some condition(s) is/are true

# as an example, this while loop keeps generating a random number between 1 and 100 until the random number is even
number = 1
while number % 2 == 1:
    print("Current value of Number: ", number)
    number = random.randrange(1, 100, 1) # arguments: beginning of range, end of range, step
print("Final Number: ", number)

# break statements will automatically break out of a loop
number = 1
while number % 2 == 1:
    print("Current value of Number: ", number)
    if(number % 5 == 0):
        print("Wow! Number is divisible by 5, crazy stuff")
        break # automatically breaks out of the loop
    number = random.randrange(1, 100, 1) # arguments: beginning of range, end of range, step
print("Final Number: ", number)

print("====================================================")

# write a while loop that randomly generates a number UNTIL that number is divisible by 3. If the number is divisible
# by 10, however, go ahead and prematurely get out of the loop
num = 1
while num % 3 != 0:
    print("Current value of num: ", num)
    if num % 10 == 0:
        break
    num = random.randrange(1, 100, 1)

''' While Loops '''
print("***************************************************************************************************************")
print()

print("For Loops + Range() Function")
print("***************************************************************************************************************")
''' For Loops + Range() Function '''

# if you want to perform a function a known amount of times, that is what for loops are for!

# lets say we wanted to print the numbers 1-10
# both of the following for loops perform the same task:

for i in range(1, 11, 1):
    print(i)
print("-----------------")
for i in range(1, 11):
    print(i)
print("-----------------")

# the range function takes 3 arguments
# 1. The beginning number
# 2. The number you want to end at (as in, when you reach that number NOTHING will hapen
# 3. (Optional) how much you want to increment the counter

# lets say we want to print all numbers divisible by 5 up to 25
for i in range(5, 26, 5):
    print(i)

print("====================================================")

# write a four loop that prints all numbers divisible by 3 up to 30

for i in range(3, 31, 3):
    print(i)

''' For Loops + Range() Function '''
print("***************************************************************************************************************")
print()
