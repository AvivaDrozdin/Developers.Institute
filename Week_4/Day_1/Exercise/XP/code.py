#Exercise 1
print('Hello World \n'*3)

#Exercise 2
calculation = int((99^3) * 8)
print(calculation)

#Exercise 3
5 < 3 #expected outcome false - actual outcome false
3 == 3 #expected outcome true - actual outcome true
3 == '3' #expected outcome true - actual outsome false /int & str
 #expected outcome false -actual error (on python 3. on python 2 false)
'Hello' == 'hello' #expected outcome false

#Exercise 4
computer_brand = 'Dell'
print(f'I have a {computer_brand} computer')

#Exercise 5
myname = 'Aviva'
age = 25
shoe_size = 39
info = (f'Hi, I am {myname}, I am {age}. I so far lived in 6 countries, and keep traveling the world with my huge {shoe_size} sized feet')

print(info)

#Exercise 6
a = 20
b = 10

if a > b:
    print('Hello World ')
else:
    print('goodbye')

#Exercise 7
number = int(input('Give me a number '))

if (number % 2) == 0:
    print('Even')
else:
    print('Odd')

#Exercise 8
person = input('What is you name? ')

if person != myname:
    print('IMPOSTER!')
else:
    print('Hello me')

#Exercise 9
inch = float(input('What is your hight in inches?'))
centimeter = 2.54*inch
height = 145

if centimeter > height:
    print('Happy ride')
else:
    print('too short')