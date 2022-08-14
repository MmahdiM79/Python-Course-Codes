from os import system
system('clear')




### Strings methods ###

string = 'this is a string example\n for PythoN String Methods\n'
print('main string:', string, '\n')


# swapcase() - swaps the case of the string
print('swapcase method output: ', string.swapcase())


# strip() - strips the string of whitespace
print('strip method output: <', '    abc    '.strip(), '>', sep='')

# rstrip() - strips the string of whitespace from the right
print('rstrip method output: <', '    abc    '.rstrip(), '>', sep='')

# lstrip() - strips the string of whitespace from the left
print('lstrip method output: <', '    abc    '.lstrip(), '>', sep='')


print('\n')


# partition() - splits the string at the first occurrence of the separator
print('partition method output: ', string.partition('ring'))
print('partition method output: ', string.partition('test'))

# rpartition() - splits the string at the last occurrence of the separator
print('rpartition method output: ', string.rpartition('ring'))


print('\n')


# split() - splits the string at the first occurrence of the separator
print('split method output: ', string.split())
print('split method output: ', string.split('ring'))
print('split method output: ', string.split('ring', maxsplit=1))
# print('split method output: ', 'a  b c    d'.split())
# print('split method output: ', 'a  b c    d'.split(' '))

# rsplit() - splits the string at the last occurrence of the separator
print('rsplit method output: ', string.rsplit())
print('rsplit method output: ', string.rsplit('ring'))
print('rsplit method output: ', string.rsplit('ring', maxsplit=1))


print('\n')


# splitlines() - splits the string at line breaks
print('splitlines method output: ', string.splitlines())
print('splitlines method output: ', string.splitlines(keepends=True))


print('\n')


# encode() - encodes the string into bytes
print('encode method output: ', string.encode())
print('encode method output: ', string.encode('ascii'))
# print('encode method output: ', 'سلام'.encode('ascii'))
# print('encode method output: ', 'سلام'.encode('ascii', errors='ignore'))
# print('encode method output: ', 'سلام'.encode('ascii', errors='replace'))


print('\n')


# is...() - returns true if the string is...
print('isascii method output: ', 'سلام'.isascii())
print('isprintable method output: ', '\t'.isprintable())
print('istitle method output: ', 'This Is a Title'.istitle())
print('isidentifier method output: ', '0hello'.isidentifier())
print('isidentifier method output: ', '_hello'.isidentifier())
print('isidentifier method output: ', 'if'.isidentifier())


print('\n')


# zfill() - fills the string with zeros on the left
print('zfill method output: ', '31'.zfill(5))
print('zfill method output: ', '+1'.zfill(5))
print('zfill method output: ', '-1'.zfill(5))
print('zfill method output: ', 'hel'.zfill(5))


print('\n')


# rfind() - returns the last index of the substring in the string
print('rfind method output: ', string.rfind('ring'))

# rindex() - like rfind() but raises ValueError when the substring is not found
print('rindex method output: ', string.rindex('ring'))