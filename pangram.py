#  Write a Python function to check whether a string is pangram or not.

import string
import re

def isPangram(our_str):
    alphabet = string.ascii_lowercase
    our_str = re.sub('[^a-z]', '', our_str.lower())

    for char in alphabet:
        if char not in our_str:
            return f'The String is not a Pangram: {False}'
    return f'The string is a Pangram: {True}'

if __name__ == '__main__':
    our_str = input('Enter your string: ')
    result = isPangram(our_str)
    print(result)