# Write a Python function that checks whether a word or phrase is palindrome or not.

def isPalindrom(string):

    string = string.replace(" ", "").lower() # remove spaces and lower the string
    reversed_string = string[::-1] # reverse the string

    #  compare the given string to reversed string
    if string == reversed_string:
        return f"The string is a Palindrome"
    return "The string is not a palindrome"

if __name__ == '__main__':
    string = input("Enter a string: ")
    result = isPalindrom(string)
    print(result)


