#Exercise 1
print('Hello World \n'*3 + 'I love Python\n'*3)

#Exercise 2
month = int(input('What month number is it? '))

if month >=3 and month <= 5:
    print('Spring runs from March to May ')

elif month >=6 and month <=8:
    print('Summer runs from June to August')

elif month >=9 and month <=11:
    print('Autumn runs from September to November')

else:
    print('Winter runs from December to February')