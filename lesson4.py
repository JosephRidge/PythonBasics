"""
- Loops
- Functions (parametrized, non parametrized, anonymous )
- Intro to Object Oriented Programming (class)

"""
import hashlib

output = "" # global variable
# for i in range(10):
#     print(i)

fruits = ["apple", "mango","pineapples", "kiwi"] 

for fruit in fruits:
    output += fruit 

for index, fruit in enumerate(fruits):
    output += "{index+1}: {fruit}"

# while

name = "John Doe"
x = 0 

while(x <= 10):
    output += str(x)
    x+=1

x = 0
while(x < len(name)):
    output += name[x]
    x+=1

"""
Functions: 
    - has the keyword 'def' or 'lambda' for anonymous functions
    - types:
        - Parameterized
        - Non-Parameterized
        - anonymous functions
    - Rule:
        - must achieve only one purpose (single purpose only) BEST PRACTICE
"""

# a simple non parameterized functions that does only one thing 
#  declare a function
def greeting():
    print("Hello world!")

# function that does something and returns somehting
def morningGreetings():
    return "Good morning!"

# a simple parameterized functions that does only one thing 
def customMorningGreetings(name:str):
    return f"Good morning {name}!"

def personalBio(name:str, age:int, height:float):
    return f"Good morning, my name is {name}. I am {age} yrs old. I am {height} cm tall!"

# call a function to run it
# greeting()
output = morningGreetings()
output = customMorningGreetings("Sun")
output = personalBio("Mr Sun", 100, 120)
output = personalBio(name="Mr Sun YU", age=100, height = 120)

"Kayak" 

def palendromTest(word):
    if word == word[::-1]:
            return " Is Palendrom"
    else:
        return "Not Palendrom"

#  anonymous functions =>  lambda functions
x = lambda a: a*10 # anonymous functionf
format_mail = lambda mail: mail.upper()

user_email = "abCDE@gmail.com"#input("Enter your email: ") 
user_email = format_mail(user_email)

output = user_email

check_palendrom = lambda text: palendromTest(text)
output = check_palendrom("Look")



# print(len("Hello World  "))
# print(len("Hello World"))
output = "Hello World  ".rstrip()
output = len(output)


#  Simularing a simple login situation simulation
def userInputs():
    email = input("Enter your email: ") # local variable
    password = input("Enter your password: ") # local variable
    return (email, password)

email, password = userInputs() 

#  clean the input
# - remove trailing spaces
# - for email change to lower case
def cleanInputs(user_input, choice):
    if choice == 'email':
        return user_input.lower().rstrip()
    else:
        user_input = user_input.rstrip()
        user_input = hashPassword(user_input)
        return user_input #removes space at the end

# function to hash the password 
def hashPassword(password):
    password = password.encode(encoding = 'UTF-8', errors = 'strict') 
    return hashlib.sha256(password).hexdigest()

#  main credentials saved in Database
email_on_DB = "abc@gmail.com"
password_on_DB = hashPassword("password254")

login = lambda e, p:(( e == email_on_DB) and (p == password_on_DB))

email_input = lambda e: cleanInputs(e, "email")
password_input = lambda p: cleanInputs(p, "password")
# output = f"[{email_input(email )}] [{password_input(password)}]"
# print(output)

print("--" *50)
print("DATABaSE DETAILS")
print(email_on_DB)
print(password_on_DB)
print("--" *50)

print("==" *50)
print("USER INPUTS")
print(email_input(email))
print(password_input(password))

print("==" *50)

#  login 
if(login(email_input(email), password_input(password))):
    output ="Welcome BACK!"
else:
    output = "Oops! wrong credentials "

print("==" *50)
print(output)
print("==" *50)