

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
'''
