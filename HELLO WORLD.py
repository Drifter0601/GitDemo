print("hello world,my name is chethan")
print('*' * 10)
price = 10
price = 20
print(price)
rating = 4.9
name = 'chethan'
is_published = True
name ='John Smith'
age = 20
is_new =True
name = input('What is your name?')
color = input('What is your favorite color?')
print(name + " likes " + color)
dob = input('Birth year?')
age= 2023 -int(dob)
print(age)
weight_lbs = input('What is your weight?')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
course = """
Hi chethan,
here is our first email to you.
thank you,
support
"""
print(course)
course = "python for beginners"
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[1:])
name = "chethan"
print(name[1:-1])
first_name = "chethan"
last_name = "Reddy"
msg = f'{first_name} [{last_name}] is a color'
print(msg)
course = "python for beginners"
print(len(course))
print(course.upper())
print(course.find('p'))
print(course.replace('beginners','absolute beginners'))
print('python' in course)
print(10+3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)
x = 10
x = x+3
print(x)
x = 10+3*2
print(x)
#parenthesis
#exponentiation
#multiplication or division
#addition or substraction
x = 2.9
print(round(x))
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day")
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: {down_payment}")
has_high_income = True
has_good_credit = False
has_criminal_record = True
if has_high_income and has_good_credit:
    print("eligible for loan")
if has_high_income or has_good_credit:
    print("eligible for loan")
if has_high_income and not has_criminal_record:
    print("eligible for loan")
temp = 35
if temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
name = "Chethan"
if len(name)<3:
    print("name must be atleast 3 chars")
elif len(name) > 50:
    print("name must be less than 50 chars")
else:
    print("name looks good")
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight/0.45
    print(f"You are {converted} pounds")
i=1
while i < 5:
    print('*' *i)
    i=i+1
print("done")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count+=1
    if guess == secret_number:
        print('you won')
        break
else:
    print("Sorry you failed")
command = "" #creates empty string
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("car stopped")
    elif command =="help":
        print(""""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("Sorry I don't uderstand that")
#FOR LOOP:
for item in 'Python':
    print(item)
for item in ['Mosh','John','Sarah']:
    print(item)
for item in range(10):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5,10,2):
    print(item)
total = 0
for item in [10,20,30]:
    total =total+item
print(f'total:{total}')
#Nested loop:
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)
#lists:
names = ['John','Bob','Mosh','Sarah','Mary']
print(names[-2])
print(names[2:])
names[0] = 'Jon'
print(names)
numbers = [12,3,6,11,8,4,10]
max = numbers[0]
for x in numbers:
    if x>max:
        max=x
    else:
        max = max
print(max)
# 2D lists: applications in data science and machine learning.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])
for row in matrix:
    for item in row:
        print(item)
#List Methods:
numbers = [5,2,1,7,4]
numbers.append(13)
print(numbers)
numbers.insert(0,10)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(5))
numbers2 = numbers.copy()
print(numbers2)
numbers = [2,2,4,6,3,4,6,1]
unix = []
for number in numbers:
    if number not in unix:
        unix.append(number)
print(unix)
#Tuples: can not be modified
numbers = (1,2,3)
print(numbers[0])
#Unpacking works both for lists and tuples.
coordinates = (1,2,3)
x,y,z = coordinates
print(x)
print(y)
print(z)
#Dictionaries
customer = {"name":"Chethan","age":30,"is_verified":True}
print(customer.items())
print(customer.keys())
print(customer.values())
print(customer["name"])
print(customer.get("birth_date","jan 1 1980"))
customer["name"] = "Chintu"
print(customer["name"])
phone = input("phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seaven",
    "8":"Eight",
    "9":"Nine"}
output = ""
for ch in phone:
    output= output+digits_mapping.get(ch,"!") + " "
print(output)
#Functions:
def greet_user():
    print('Hi there!')
    print('Welcome aboard')


#parameters:
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')


greet_user("john")
#keyword Argument:Order of arguments does not matter
def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


greet_user(last_name = "Reddy",first_name = "Chethan")
def square(number):
    return number * number
print(square(3))
result = square(3)
#by default if return is not there the function returns "None"
#Creating the usable function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output

message = input("> ")
print(emoji_converter(message))
#Exception:
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
#classes:
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)
#Constructors:

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y  #constructor init method.
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point = Point(10,20)
print(point.x)
point.x = 11
print(point.x)


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")
john = Person("John Smith")
john.talk()
#inheritance:
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")
class cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()
#import ecommerce.shopping
#ecommerce.shopping.calc_shipping()
#from ecommerce.shopping import calc_shipping
#Generating random values:
import random
for i in range(3):
    print(random.random())
for i in range(3):
    print(random.randint(10,20))
members = ['John','Mary','Bob','Mosh']
print(path.rmdir())
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first,second



dice = Dice()
print(dice.roll())
# Files and directories
from pathlib import Path
#Absolute path
#c:\Program Files\Microsoft
#\usr\local\bin
#Relative path
path = Path("ecommerce")
print(path.exists())





















































