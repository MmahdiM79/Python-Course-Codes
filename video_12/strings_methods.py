from os import system
system('clear')




### Strings methods ###

string = 'this is a string example for Python String Methods'
print('main string:', string, '\n')

# capitalize() - converts the first character of each word to upper case
print('capitalize method output: ', string.capitalize())

# title() - converts the first character of each word to upper case
print('title method output: ', string.title())

# upper() - converts all characters to upper case
print('upper method output: ', string.upper())

# lower() - converts all characters to lower case
print('lower method output: ', string.lower())



print('\n')



# replace() - replaces a string with another string
print('replace method output: ', string.replace('Python', 'Java'))
# print('replace method output: ', string.replace('python', 'Java'))
# print('replace method output: ', string.replace('i', '?'))
# print('replace method output: ', string.replace('i', '?', 2))

# count() - counts the number of times a substring occurs in the string
print('count method output: ', string.count('i'))
print('count method output: ', string.count('i', 5, 13)) # slice [5:13]


print('\n')


# find() - returns the index of the first occurrence of a substring
print('find method output: ', string.find('i'))
print('find method output: ', string.find('i', 5, 13)) # slice [5:13]
print('find method output: ', string.find('mamad'))

# index() - returns the index of the first occurrence of a substring
print('index method output: ', string.index('i'))
print('index method output: ', string.index('i', 5, 13)) # slice [5:13]
# print('index method output: ', string.index('mamad'))



# print('\n\n----------------------\n\n')

### What is immutable? ###

# wrong way to change a string
# print(string)
# string.upper()
# print(string)

# right way to change a string
# print(string)
# string = string.upper()
# print(string)