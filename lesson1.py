# this is a one-liner comment

"""
This is a multi-line string 
It can also be used as a multi-line comment
"""

"""
Variables: A reference to somehting that has been stored in memory
Types of variables based on scope: 
    - Global variables(accessible throughout the entire script/ source code)
    - Local variables(only accessible to where they have been defined)
Variables can be immutable(you cannot change the value we tend to use ENUM classes) or mutable(you can redefine them) in nature
Rule: 
    - You cannot use a variable unless it has been defined
"""

CONST_NAME = "abc" # this is how we would distinguish constant and non constrant values
 

# name # this is a vairable without definition hence will bring an error(NameError: name 'name' is not defined)
output = "" # Global variable
age = 10   
age = 100
output = age # redefining 

output = CONST_NAME 
# age = input() # is a standard input whereby the user will enter a value...
output = age


age = input("Enter your age: ") # returns a string in nature
output = age
output = 200 # number

output = type(output) # the type function checks the data type


# standard ouput: obligated ot return or give an output to the user/actor
print("==========================================================")
print(output)
print("==========================================================")# print("="*10)