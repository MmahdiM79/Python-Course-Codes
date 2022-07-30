from os import system
system('clear')




### Escape sequences ###

# \a - alert
# print('a\a')

# \b - backspace
# print('ab\bcd')

# \f - formfeed
# print('abcd\fefg')

# \n - newline
# print('abcd\nefg')

# \r - carriage return
# print('abcd\rxyz')

# \t - tab
# print('abcd\txyz')

# \v - vertical tab
# print('abcd\vxyz')

# \' - single quote
# print('abcd\'xyz')

# \" - double quote
# print("abcd\"xyz")

# \\ - backslash
# print('abcd\\xyz')

# \0 - null
# print('abcd\0xyz')




### ASCII vs Unicode ###
# ASCII - 7-bit ASCII (128 characters)
#   example: 'a' = 97, 'z' = 122
#
# Unicode - 16-bit Unicode (2^16 characters)
#   example: 'a' = U+0061, 'z' = U+007A

# print('\N{BLACK STAR}')
# print('\N{yawning face} \N{minibus}')
# print('\N{WHITE STAR}')





### Strings operations ###

a = 'Hello'
b = 'World'
c = 'Media'

# print(a + ' ' + b + ' ' + c)

# print(a + ' ' + 3)
# print(a + ' ' + str(3))

# print((a + ' ' + b + ' ' + c + '\n') * 4)
# print((a + ' ' + b + ' ' + c + '\n') * 4.5)

