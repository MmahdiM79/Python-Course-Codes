from os import system
system('clear')


a = 10
b = 17

# swap: a -> 17 and b -> 10


# WRONG SOLUTION:
# a = b
# b = a
# print('a =', a, 'and b =', b)


# 1st CORRECT SOLUTION:
# temp = a
# a = b
# b = temp
# print('a =', a, 'and b =', b)



# 2nd CORRECT SOLUTION:
# a, b = b, a
# print('a =', a, 'and b =', b)



# 3rd CORRECT SOLUTION:
# a = a + b
# b = a - b
# a = a - b
# print('a =', a, 'and b =', b)