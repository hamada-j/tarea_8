

from django.apps import AppConfig


class HelloWorldConfig(AppConfig):
    name = 'hello_world'

'''

STRING
course = 'Python for Biginners'
len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
'...' in course

MATH OPERATORS
print(10+3)
print(10-3)
print(10/3)
print(10//3)
print(10*3)
print(10**3) power
print(10%3) Modul

MATH METHODS
x = 10
x *= 3
print(x)
-----------------
x= 2.8
print(round(x))
-----------------
import math
print(math.floor(2.9))

STATMENTS
is_hot = True
is_colde = True

if is_hot:
    print('It is a hot day')
    print('drink pleanty of water')
elif is_colde:
    print('its a cold day')
    print('drink warm of water')
else:
    print('enjoy your day')

AND & OR & NOT OPERATORS
And(both true) or(one true)
has_high_income = False
has_high_credit = True

if has_high_income or has_high_credit:
    print('Eligible for loan')

------------------------------------------

has_high_income = True
has_high_credit = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print('Eligible for loan')


OPERATORS < > <= >= == !=

name = input('please input your name: ')
if len(name) < 3:
    print(f'name must be at least 3 characters,\n your input is: "{name}"')
elif len(name) > 8:
    print(f'{name}, must be a maximum of 8 characters')
else:
    print(f'user-name: {name} looks good')

weight = input('your wight: ')

lbs_or_kg = input('l or k: ')

if lbs_or_kg == 'k':
    print(f'your weigth is {int(weight) * 2 }Lb')
elif lbs_or_kg == 'l':
    print(f'your weigth is {int(weight ) / 2 }Kg')

LOOP
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('done')

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('done')

GAME
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You wont!')
        break
else:
    print('Sorry, u filed')



MY GAME
input_gamer = input('> ')

start_car = print('start')
stop_car = print('stop')
quit_game = print('quit')

guess_count = 0
guess_limit = 8

while guess_count < guess_limit:
    input_game = input('> ')
    guess_count +=1
    if input_game == 'start':
        print('start dreving the car')
    elif input_game == 'stop':
        print('stop the car')
    elif input_game == 'quit':
        print('quit game')
        break

MOHS GAME

command = ''
started = False
while True:
        command = input('> ').lower()
        if command == 'start':
            if started:
                print('car alred start')
            else:
                started = True
                print('car start driving')
        elif command == 'stop':
            if not  started:
                print('car is alredy stopped')
            else:
                started = False
                print('car stopped')
        elif command == 'help':
            print("""
            start - to start the car
            stop - to stop the car
            quit - quit the game """)
        elif command == 'quit':
            break
        else:
             print('sorry try agin')


FOR LOOP
for item in 'Python':
    print(item)

for item in ['MOSH', 'JOHN', 'MARTA']:
    print(item)

for item in [1,2,3,4,5,6,7,8,9]:
    print(item)


RANGE Function
(0 to 10)
for item in range(11):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

SHOP CART

MY
prices = [10,20,30]
result = 0
for item in prices:
    result += int(item)
print(result)

MOSH
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f'Total: ${total}')

NASTY LOOP
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


MY
numbers = [5,2,5,2,2,10,11]
for num in numbers:
    for element in range(num-1,num):
        print((int(element) + 1) * 'x')
MOSH
numbers = [5,2,5,2,2,10,11]
for x_count in numbers:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)

LISTS
name = ['Jhon', 'Bob', 'Mosh', 'Hamada']
name[0] = 'Jon'
print(name[1:3])
print(name)

MY
numbers = [1,2,33,4,55,6,7,8]
print(max(numbers))

MOSH
numbers = [1,2,33,4,5,6,7,8]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)


TWO DIMENSIONAL LIST [[MATRIX]]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 10
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

matrix = [5, 2, 1, 1, 1, 1, 7, 4, 20]
matrix.insert(0, 10)
matrix.remove(2)
matrix.pop()
matrix.sort()
matrix.reverse()
matrix2 = matrix.copy()
matrix.append(12)
print(matrix)
print(matrix2)
print(matrix.count(1))
print(33 in matrix)
matrix.clear()

MY
matrix = [5,5, 2, 1, 1, 1, 7,7, 4, 20]
for num in matrix:
    print(matrix.count(num))
    if matrix.count(num) != 1:
        matrix.remove(num)
print(matrix)

MOSH

matrix = [5,5, 2, 1, 1, 1, 7,7, 4, 20]
uniques = []
for number in matrix:
    if number not in uniques:
        uniques.append(number)
print(uniques)


TOPLIST

coordinates = (1,2,3)
2 Normal methods Count and Index

__MagicMethods



UNPAQUING

coordinates = (1,2,3)
----
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
----- igual que lo anterior
x, y, z = coordinates
----

coordinates = [1, 2, 3]
coordinates = (1, 2, 3)
x, y, z = coordinates
print(z)


DICTIONARY: KEY_VALUE

customers = {
    'name': 'John',
    'age': 35,
    'is_verified': True
}
customers['birthdate'] =  'Jan 1 1980'
print(f"{customers['age']} years old")
print(customers)

MY

phone = input('phone: ')
numbers2 = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

for num in phone:
    print(numbers2[int(num)])


MOSH
phone = input('Phone: ')

digits_mappping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three'
}

output = ''

for ch in phone:
   output += digits_mappping.get(ch, '!') + ' '

print(output)

message = input('>')
words = message.split(' ')
emojis = {
    ':)': '🤣',
    ':|': '🤨',
    ':(': '😞',
    ';)': '😉'
}
output = ''
for word in words:
  output +=  emojis.get(word, word) + ' '

print(output)


FUNCTIONS
def greet_user(name, age):
    print('Hi there!')
    print(f'Welcome aboard {name}, {age} years old')


print('Start')
name = input('Your name: ')
age = input('Your age: ')
greet_user(name, age)
print('Finish')

def greet_user(name, age):
    print('Hi there!')
    print(f'Welcome aboard {name}, {age} years old')


print('Start')
greet_user(age= '12', name='hama')
print('Finish')

Sin el return devuleve NONE === NULL
por defecto las funciones en Python devuleven NULL
def square(number):
    return number * number

print(square(3))


WITH FUNCTIONS
message = input('>')

def function_words(message):
    words = message.split(' ')
    return words

def funcition_emojis():
    output = ''
    words = function_words(message)
    emojis = {
        ':)': '🤣',
        ':|': '🤨',
        ':(': '😞',
        ';)': '😉'
    }
    for word in words:
      output +=  emojis.get(word, word) + ' '
    return output


print(funcition_emojis())


EXCEPTION (TRY EXCEPT)

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0')
except ValueError:
    print('Invalid value')

COMMENTS
# this is a comment

# method print value
print('Sky is blue')

CLASSES

Numbers
Stirngs
Booleans
----
Lists
Dictionaries

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
print(point1.y , point1.x)

class Person:
    def __init__(self, lenguje):
        self.lenguaje = lenguje

    def tolk(self):
        print(f'I speak  {self.lenguaje}')

some_one = Person('ingles')
print(some_one.lenguaje)
print(some_one.tolk())


INHERETENS -- SubClass --

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def be_nace(self):
        print('walk')

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.be_nace()
dog1.walk()

MODULES
import converters
from converters import kg_to_lbs

kg_to_lbs(100)
print(converters.kg_to_lbs(70))


from data import numbers
from utils import find_max

print(find_max(numbers))
'''

