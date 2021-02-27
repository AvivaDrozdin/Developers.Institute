#1
l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']

#2
number = []

number.append(int(input('The first number is: ')))
number.append(int(input('The second number is: ')))
number.append(int(input('The third  number is: ')))

print(f'The biggest number is {max(number)}')

#3 counter
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range (len(alphabet)):
    if alphabet[i] in vowels:
        print(f'{alphabet[i]} is a vow')
    else:
        print(f'{alphabet[i]} is a const')

#4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

for nam in names:
    nam = str(input('Give me a name: '))
    if nam in names:
        print(names.index(nam))
        continue 
    elif nam == 'exit':
        break
    else:
        names.append(nam)

print(names)

#5
words = []
ask =  str(input('Give me 7 words seprarated by comma: '))

words = ask.split(',')


print(words)