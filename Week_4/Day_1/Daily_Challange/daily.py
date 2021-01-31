words = input('Type in some words - 10 charecters max! ')


if len(words)<10:
    print('Sorry, string not long enough')

elif len(words)>10:
    print('Ups, string too long')

else:
    blank=''
    for x in range (0, len(words)):
        blank+=words[x]

        print(blank)



