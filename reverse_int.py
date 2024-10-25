#  Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def reverse_integer(num):

    reversed_int_str = str(abs(num))[::-1] # convert num to string, remove negative and reverse it

    # check if num is negative
    if num < 0:
        # convert back to int and restore the sign if negative
        return int(reversed_int_str) * -1
    return int(reversed_int_str)

if __name__ == "__main__":
    num = int(input("Enter an Integer: "))
    result = reverse_integer(num)
    print("Reversed integer: ", result)
