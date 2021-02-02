shift = int(input('Shift by: \n'))

text = str(input('Encrypt this: \n'))

encrypt = ""

for letter in text:

    encrypt += chr(ord(letter) + shift) #shifts by the amount of shifts be chose

print(f'Your encryption: \n {encrypt}')



decrypt = ""

for letter in encrypt:
    decrypt += chr(ord(letter) - shift)

print(f'The decryption is: \n {decrypt}')