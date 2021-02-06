
def reverse_bits(num, bit_size):

    #1)Convert nr to binary
    binary = bin(num)

    #2) skip the first two characters of binary representation string and reverse.
    #3) remaining string and then append 0’s after it.
    #4) from the last character and reverse it until second last character from the left.
    reverse = binary[-1:1:-1]       
                                        
    reverse = reverse + (bit_size - len(reverse))*'0'

    #5) converts reversed binary string into an integer.
    print(int(reverse,2))

reverse_bits(1234, 32)





