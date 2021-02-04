#matrix = list with lists inside
matrix = [
    ['7','i','3'],
    ['T', 's', 'i'],
    ['h', '%' ,'x'],
    ['i',' ','#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    [' ', 'r', '!']
]


decryption = ''
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[j][i].isalpha() or matrix[j][i] == ' ':
            decrypt += matrix[j][i]

print(decryption)