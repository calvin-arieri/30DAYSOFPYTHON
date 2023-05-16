

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
# Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 
number_1 = int(input("enter a number: "))
number_2 = int(input("enter second number: "))

def sumFunction():
    print("sum of numbers", number_1 + number_2)


def differenceFunction():
    print("subtraction of numbers", number_1 - number_2)

def divisionFunction():
    print("divide two numbers", int(number_1/number_2))

def powerFunction():
    print("powering the two numbers", pow(number_1, number_2))

def deletionFunction():
    number_1 = 0
    number_2 = 0
    print("number 1 deleted", number_1)
    print("number 2 deleted", number_2)
powerFunction()                 
divisionFunction()    
sumFunction()
differenceFunction()  
deletionFunction()  