#1 Formula
import math

c = 50
h = 30
#total = []
number = [num for num in input('assign values for d, separated by a comma: ').split(',')]

for d in number:
    print(int(math.sqrt(2*c*float(d)/h)))

#2 
l1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
l2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
l3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
l4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]


#l_join = ','.join(str(i) for i in l1)

#a
print(f'The list of numbers: ' + ','.join(str(i) for i in l1))
#b


#Paragraph
para = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor. Incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

# how many char
def count_char(para):
    for i in range(len(para)):
        count = 0
        while count <= len(para):
            count += 1
    print(f'The paragraph contains {count} characters')

#how many sentence
def count_sent(para):
    split = para.split('.')
    for i in range(len(split)):
        count = 0
        while count <= len(split):
            count += 1
    print(f'The paragraph countains {count} sentences')

#how many words
def count_word(para):
    #split = para.split(' ')
    alpha = para.isalpha()
    for i in range(len(alpha)):
        count = 0
        while count <= len(alpha):
            count += 1
    print(f'The paragraph countains {count} words')

#how many unique words

