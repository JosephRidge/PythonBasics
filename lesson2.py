"""
DATA TYPES: 
- Tell how we can store things in memory(basically the structure)
- influenced by ASCII Table(https://www.asciitable.com/)
- It stems from a class(basically a blue-print to create a real world thing object) and when we create a variable we actually create an instance of that class making an object
- Types: 
    - Number (Integers & Floating)
    - Text (String)
    - Lists (arrays, tuple, set)
    - Dictionary
"""

#  Number (Integers & Float)
"""
Integer:
    - a whole number(no decimal) that spans from -ve infitnity to +ve infinity 
    - class: <class 'int'>

Contains a couple methods that enable it to perform a particular objective

"""

output ="" # this is our global variable
age  = 100 
output = type(age) # checking the data type of age

# age = input("Tell me your age: ") # gives us a string type of data
output = age
output = type(age) # checking the data type of age

output = int(age) # casts the data type to an interger 
output = type(output) # checking the data type of age


#  methods: This is function that resides inside a class. A function is a series of statements that do one particular task(BEST practice-single purpose only [look at cleancode by uncle Bob and Pragmatic programmer])

"""

Floating point numbers: 
    - They are continous numbers(has decimal places)
    - class: <class 'float'>
"""

temperature = 32.75
humidity_level = 40.45

output = type(temperature) # checking the data type
output = int(temperature) # we are converting from float to int => truncates the decimal

# ouput = type(output)  # this is a delibearate type on the "output" variable to express how python does not automatically correct your variable namee
# output = type(output) 
output = float(output)
output = complex(output)


"""
Complex numbers: 
    - These represent complex numbers from a mathematical standpoint eg the outocme of thw sqrt of 2 that will be a complex number
    - class:  <class 'complex'>
"""
root = 2j 
output = type(root)


"""
Text:
    - This is a collection of characters
    - class: <class 'str'>

Rule: 
    - it can be enclosed in either 'single quotes' or "double quotes" or """"""

Methods: 
- toUpper()
- toLower()
- isin()

"""

first_name = "John Doe"  
second_name = 'Mark'
last_name = "M"

output = first_name
output = type(first_name)
output = type(second_name)
output = type(last_name)

output = first_name[0]   # accessing first element within the string 
output = first_name[-1]  # accessing last element within the string 

# Slicing
output = first_name[0:4] # it will slice the string and start from position 0 to position 3
output = first_name[0:5] # it will slice the string and start from position 0 to position 4
output = first_name[2:]  # it will slice the string and start from position 2 to the end
output = second_name[-3:]

# Slicing with a step
output = first_name[0: 8: 2] # start counts from position 0 to last positoin but wit a step of 2
output = first_name[0: 8: 3] # start counts from position 0 to last positoin but wit a step of 3

output = len(first_name) # gets the size of a string
 
print("="*50)
print(output)
print("="*50)

