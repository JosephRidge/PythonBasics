"""
DATA TYPES: 
- Tell how we can store things in memory(basically the structure)
- influenced by ASCII Table(https://www.asciitable.com/)
- It stems from a class(basically a blue-print to create a real world thing object) and when we create a variable we actually create an instance of that class making an object
- Types: 
    - Number (Integers | Floating | Complex)
    - Text (String)
    - Boolean
    - Lists (arrays, tuple, set)
    - Dictionary

Good read:https://docs.python.org/3/tutorial/introduction.html#
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

refer to this: https://www.w3schools.com/python/python_strings_methods.asp
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
 
#   methods
station_name = "Kipro"
# abc@example.com equal to ABC@example.com
email = "abc@example.com"

output = station_name.rindex("p") # returns the index
output = email
output = email.upper()
output = email.lower()
output = email.endswith("m") #  this acts as a predicate(returns either True or False)

"""
if we were not to use rindex() we would run it like this: 
    - get the string 
    - get the target string/ character you want to search for
    - assign the starting index = 0
    - check the first element
    - if element is equivalent to the target character we stop 
    - else add one to the index and continue the search
"""

i = 0
target_char = "p"
station_name = station_name.lower()

for character in station_name:
    # print(character)
    if target_char == character:
        break
    else:
        i = i + 1
    
output = i

first_name = "John"
second_name = "Kamau"
last_name = "Doe"

output = first_name + " " + second_name + " " + last_name # concatenation
output = f"{first_name} {second_name} {last_name}"


"""
Boolean:
    - simply a True or False statement/ outcome
    - can be triggered when testing conditions or invoking predicates
    - class: <class 'bool'>

Rule: 
    - always start your naming as though yo are questioning the outcome eg is_fan_on
"""

isCold = True 

output = isCold
output = type(isCold)

"""
Truth table

"""
isCold = True
hasSweater = False 

if (isCold and not hasSweater):
    output = "you will be ok!"
else:
    output = "flue on thre rise!"

output = isCold
output = not isCold # not negates the outcome of the inital definition

# example working with reange 
output = ""
for i in range(1,10, 2):
    output = output +  str(i)  # this can also be written as output += str(i)

"""
Lists:
    - collection of items/ elements
    - Types: 
        - array
        - Tuple
        - Set
    - counting starts from  hence we use index for positional access
    - they are mutable however a string is immutable despite being a list
"""

"""
array list
    - enclosed within []
    - contains its own methods
    - we access elements using index

Methods: https://www.w3schools.com/python/python_lists_methods.asp

"""

fruits = ["apple", "mango","pineapples", "kiwi" ] # best practice to have single type of data in list
output = fruits
# lusst with different data types
# fruits = ["apple", "mango","pineapples", "kiwi" , 1, 23, 90.99] # not best practice 
output = fruits

# for fruit in fruits:
#     print(fruit.upper())  # AttributeError: 'int' object has no attribute 'upper'

fruits.append("banana")
fruits.append("watermelon")
fruits.append("green apple")
fruits.append("oranges")
fruits.append("tangerines")

output = fruits

output = fruits [2:]
output = fruits [0:10]
output = fruits [0:10: 2]

# output = fruits[len(fruits)]
output = len(fruits)

# for index, i in enumerate(fruits): # enumerate takes up a list and assigns an index and to each 
#     print(index)

output = fruits[len(fruits) - 1]

user_name = "Avenger"

output = ""
for character in user_name:
    # print(character)
    if character == 'e':
        character = 'i'
    output += character # concetanation

# user_name [0] = 'S' # evokes an error: TypeError: 'str' object does not support item assignment hence strings are immutable lists 
output = user_name

"""
Tuples: 
    - enclosed in ()
    - immutable 
    - use for non-changeable elements
    - class: <class 'tuple'>

it contains methods: https://www.w3schools.com/python/python_tuples_methods.asp

"""

color = ("Red", "Green", "Blue")
# color = color.append("Yellow") # AttributeError: 'tuple' object has no attribute 'append'
output = type(color)


"""
Dictionary: 
    - Key: Value pair data stucture
    - fast to access due to the assignment of a key to each value
    - it cointains its own methods
    - defined using {}
"""


student = {
    "name": "John Doe", 
    "age": 12, 
    "course": "Software"
}


output = student
output = f"My name is {student["name"]}, I am {student["age"]} years old, currently studying {student["course"]}"
output = student.items() # returns a tuple of each key-value pair
output = student.values() # returns the values of the data



student = {
    "name": "John Doe",
    "age": 12, 
    "course": ["Software Engineering", "Data Analysis", "Data Structure"], 
    "hobby":{
        "wit": "reading random technical books", 
        "exercise":"cycle", 
        "creativity": "paint", 
        "extra-curriculla": "hunting bears"
    },
    "isKenyan": False
}

output = student
output = student["hobby"]
output = student["course"]

# TODO: Check loop in dictionary**

# for course in student["course"]:
#     print(course)


"""
SETS:
    - this is a collection of unique items
    - defined using {}
    - composed of mehtods such as join, union, intersect etc 


eg: 
- dataframe(can be a 2D or 1D data type)

df1 = {1,2,3,4,5,6}
df2 = {1,2,3,7,8,9}

df1 and df2 = {{1,2,3}

"""

fruits = ["apple", "mango","pineapples", "kiwi"] # best practice to have single type of data in list
output = fruits
# lusst with different data types
# fruits = ["apple", "mango","pineapples", "kiwi" , 1, 23, 90.99] # not best practice 
output = fruits

# for fruit in fruits:
#     print(fruit.upper())  # AttributeError: 'int' object has no attribute 'upper'

def addFruits(fruits):
    fruits.append("apple")
    fruits.append("mango")
    fruits.append("pineapples")
    fruits.append("banana")
    fruits.append("watermelon")
    fruits.append("green apple")
    fruits.append("oranges")
    fruits.append("tangerines")
    return fruits

addFruits(fruits)
addFruits(fruits)
addFruits(fruits)


output = fruits
output = type(fruits)

unique_fruits = set(fruits) # parsed from list to sets

output = unique_fruits
unique_fruits.pop()
unique_fruits.remove("kiwi")
output = unique_fruits


print("="*50)
print(output)
print("="*50)

