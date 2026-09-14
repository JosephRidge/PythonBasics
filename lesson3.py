"""
Operators:
    - Comparison Operators
    - assignment Operators
    - Bitwise Operators (|, || , & , &&)
    - Arithmetic (+,-,/,//,**,*)
    - Boolean (use the Truth tables to get the outcomes or 'and' , 'or', 'not',etc scenarios)

Control flows: 
    - if..else
    - match
    - if..elif..else
"""

"""
 Arithment operators: 
    - *, +,-,/,%, //, **

"""

# globale variable
output = " "

#  %  # used to check whether there exists a remainder in your data , can be used to check whether a number is even or odd
x = 10 
y = 2
y = 3
x = 115
y = 3
output = x % y 

# floor division: you divide two number and if you get a decimal value we truncate  the value

x = 9
y = 2

output = x/y
output = x // y # floor division

# power 
x = 2
p = 3

output = x ** p 


"""
Assignment Operators:
   - =, +=, -+, //=, *=, **= , %=, 

"""

x = 10
y = 11
new_val =0
 

output = x # assignment operator
new_val += x # this is the same as output = x + output
output -= x # this is the same as output = output - x
output = 10
output *= y # this is the same as output = output * y 
output /= y
output //= y
output = 12
output **= 2
output %= output




"""
Comparison Operators:
    - >,<, >=,<=, == 
    - returns a Boolean value
"""
x = 10 
y = 6

output = x > y
output = x < y
output = x == y
output = x >=y
output = x <= y

"""
Boolean operators:
    - and, or, not 
"""

x = 10
y = 6
z = 4
output = (x > y) and ( y >= z) # True and True
output = (x > y) and ( y <= z) # True and False

output = (x > y) or ( y >= z) # True or True
output = (x > y) or ( y <= z) # True or False

output = not output # negation get the opposite


"""
Control flows: 
    - if..else
    - if..elif..else
    - match 
"""

color_a = "red"
color_b = "Red"
color_c = "RED"


# simple if..else
if( color_a.lower() == color_b.lower()):
    output = "the colors are the same"
else:
    output ="not the same!"

color_b ="brown"
color_c = "gold"

# if ..elif..else
if (color_a =="Blue"):
    output = "sky blue"
elif(color_b == "BROWN".lower()):
    output = "brown!".capitalize()
else:
    output = "cannot identify the color!"

# mactch case 

color = "Green" 

match(color):
    case "Green":
        output = "Green-Light!"
    case "Red":
        output = "Stop Car!"
    case "Orange":
        output = "Get ready!!"
    case _: # default outcome if all the cases have not been met  
        output ="I am lost!"


print("="*50)
print(output)
print("="*50)





