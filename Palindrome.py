
str = input('Enter the string to be checked :') # Inputs string from the user


def palindrome(str):
    return str[::-1]


check = palindrome(str)
print("Reversed string is :",check)
if str == check:
    print("String entered is a palindrome string")
else:
    print("String entered is not a palindrome string")










