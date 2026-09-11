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







print("="*50)
print(output)
print("="*50)

