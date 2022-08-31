from copy import deepcopy
from os import system
system('clear')



# different ways to create a list
l1 = [1, 2, 3, 4, 5]
l2 = list('hello')
# l2 = list(23, 45, 67, 89)
# l2 = list(236)
l3 = [4, 5] * 2



# members of a list can be of different types
l4 = [1, 'hello', 3.14, True, [1, 2, 3], 4+5j]


# indexing and slicing
# print(l4[1])
# print(l4[-1])
# print(l4[1:4])
# print(l4[1:6:2])
# print(l4[-1:6:2])
# print(l4[::-1])



# changing a list member
# s = 'hello'
# s[0] = 'H'
# a = [1, 2, 3, 4, 5]
# a[0] = [1, 2, 3]
# print(a)
# del a[3]
# print(a)
# del a
# print(a)



# why we should use copy() method or deepcopy() function
# c = [1, 2, 3, 4, 5]
# d = c
# d[0] = 100
# print(c)
# d = c.copy()
# d[0] = 100
# print(c)
# print(d)

e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# f = e.copy()
# f[0][0] = 100
# print(e)
# f = deepcopy(e)
# f[0][0] = 100
# print(e)
# print(f)




# # in and not in operators
# print(1 in l4)
# print('mamad' in l4)
# print('mamad' not in l4)



# <, >, <=, >=, ==, != and is operators

# == and is operators
# h = [1, 2, 3, 4, 5]
# g = [1, 2, 3, 4, 5]
# i = g
# print(h == g)
# print(h is g)
# print(g is i)

# j = [1, 2, 3, 4, 5]
# # j = [1, 2]
# k = [1, 2, 4, 5, 6]
# print(j < k)
# print(j > k)
# print(j <= k)
# print(j >= k)



# + and * operators and len() function
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
# print(y + x)
# print(x + y)

print(x)
print(*x) # * operator is used to unpack a list
print(1, 2, 3, 4, 5)

print(len(x))
