import random
import string

def key_generator() -> str: # generate key in len of 7 chars with random letters and digits
    lowercase_letters = list(string.ascii_lowercase) #list with letters
    digits = list(string.digits) #list with numbers
    char_type = ['letter', 'digit']
    
    key = ''
    
    for _ in range(7):
        if random.choice(char_type) == 'letter':
            key += random.choice(lowercase_letters)
        else:
            key += random.choice(digits)
            
    return key

link = input()

data = 