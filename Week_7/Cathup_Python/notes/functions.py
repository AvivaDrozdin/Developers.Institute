# def hello():
#     print('hello')

# def bye():
#     print('bye')

# def add(num1, num2):
#     return num1 + num2


#functions require specific parameter to be executed (usually)

#create a function that takes a list of numbers as a parameter and prints the sum of the all the numbers in the list

def add(number):
    total = 0
    for num in number:
        total += num
    return total

num = [1, 2, 3]


