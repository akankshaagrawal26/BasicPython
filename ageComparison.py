import datetime

name = input('Enter your name : ')    # Inputs name from user
age = int(input('Enter your age : '))  # Inputs age from user

year = datetime.datetime.now().year + (100-age)  # Adds current year to the no. of years required to turn 100

print('You will turn 100 years old in',year)

