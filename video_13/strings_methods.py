from os import system
system('clear')




### Strings methods ###

string = 'this is a string example for PythoN String Methods'
print('main string:', string, '\n')

# casefold() - converts the string into lowercase for comparison
print('casefold method output: ', string.casefold())


print('\n')


# center() - centers the string in a field of a given width
print('center method output: ', string.center(80))
print('center method output: ', string.center(80, '_'))
# print('center method output: ', string.center(20, '-'))
# print('center method output: ', string.center(20))

# ljust() - left justifies the string in a field of a given width
print('ljust method output: ', string.ljust(80))
print('ljust method output: ', string.ljust(80, '_'))
# print('ljust method output: ', string.ljust(20, '-'))
# print('ljust method output: ', string.ljust(20))

# rjust() - right justifies the string in a field of a given width
print('rjust method output: ', string.rjust(80))
print('rjust method output: ', string.rjust(80, '_'))
# print('rjust method output: ', string.rjust(20, '-'))
# print('rjust method output: ', string.rjust(20))


print('\n')


# endswith() - returns true if the string ends with the specified suffix
# print('endswith method output: ', string.casefold().endswith('methods'))
print('endswith method output: ', string.endswith('Methods'))
print('endswith method output: ', 'test.py'.endswith(('.py', '.txt')))
print('endswith method output: ', string.endswith(('.py', '.txt'), 10, 20))

# startswith() - returns true if the string starts with the specified prefix
print('startswith method output: ', string.startswith('this'))
print('startswith method output: ', string.startswith('this', 0, 10))
print('startswith method output: ', string.startswith(('this', 'This')))
print('startswith method output: ', string.startswith(('this', 'This'), 0, 10))


print('\n')


# removesuffix() - removes the suffix from the string
print('removesuffix method output: ', string.removesuffix('Methods'))
# print('removesuffix method output: ', string.removesuffix(('.py', '.txt')))

# removeprefix() - removes the prefix from the string
print('removeprefix method output: ', string.removeprefix('this'))
print('removeprefix method output: ', string.removeprefix('This'))


print('\n')


# is...() - returns true if the string is...
print('isupper method output: ', 'ABC'.isupper())
print('islower method output: ', 'abc'.islower())
print('isdigit method output: ', '12'.isdigit())
print('isspace method output: ', '  '.isspace())
print('isalpha method output: ', 'hello'.isalpha())
print('isalnum method output: ', 'hello123'.isalnum())
print('isdecimal method output: ', '0b101'.isdecimal())


print('\n')


# expandtabs() - replaces tab characters with the appropriate number of spaces
print('expandtabs method output: ', 'a\tb'.expandtabs(2))
print('expandtabs method output: ', 'a\tb'.expandtabs(4))
print('expandtabs method output: ', 'a\tb'.expandtabs(8))
