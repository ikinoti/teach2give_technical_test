def capitalize(phrase):
    return phrase.title()

if __name__ == "__main__":
    phrase = input("Enter a string of phrase: ")
    result = capitalize(phrase)
    print(result)