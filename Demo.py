

print("hello")  # print hello

print("""This is multi-line.This is first.
This is second.
"How r u?",I asked.
""")
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{0} was playing cricket yesterday'.format(name))
print(name + ' is ' + str(age) +' yrs old')

print('{0:.5f}'.format(1.0 / 3))
print('{0:.^12}'.format('hello'))
print('{name} wrote {book}'.format(name="abc",book="aaa"))

print('What\'s '
      'your name?')

print('What\"s'
      ' your name?');

print("Hi this is python \nSecond line");

print(1 +
      3 +
      5)


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

print(tuple)
print(list)



dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


def print_max(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
#print(print_max.__doc__)
help(print_max)