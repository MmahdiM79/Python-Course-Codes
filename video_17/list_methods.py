from os import system
system('clear')




### list methods ###


# append() - add a member to the end of a list
# l = [1, 2, 3, 4, 5]
# print(l)
# l.append([3, 4])
# print(l)

# extend() - add a list to the end of a list
# l1 = [1, 2, 3, 4, 5]
# print(l1)
# l1.extend([3, 4])
# print(l1)
# l1.extend('hello')
# print(l1)

# insert() - add a member to a list at a specific index
# l2 = [1, 2, 3, 4, 5]
# print(l2)
# l2.insert(0, 100)
# print(l2)

# pop() - remove a member from a list at a specific index
# l3 = [1, 2, 3, 4, 5]
# print(l3)
# a = l3.pop()
# print(l3, a, sep=' - ')
# b = l3.pop(0)
# print(l3, b, sep=' - ')
# # c = l3.pop(30)
# # print(l3, c, sep=' - ')

# remove() - remove a member from a list
# l4 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(l4)
# l4.remove(5)
# print(l4)
# l4.remove('hello')

# clear() - remove all members from a list
# l5 = [1, 2, 3, 4, 5]
# print(l5)
# l5.clear()
# print(l5)
# # del l5 - !

# copy() - copy a list
# see video 16 please.

# count() - count the number of times a member appears in a list
# l6 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(l6.count(4))

# index() - find the index of a member in a list
# l7 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(l7.index(4, 4, 6))

# reverse() - reverse a list
# l8 = [1, 2, 3, 4, 5]
# print(l8)
# l8.reverse()
# print(l8)

# strings are immutable but lists are mutable
# s = 'hello'
# s = s.upper()
# s = s[::-1]
# print(s)

# sort() - sort a list
# l9 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# l9.sort()
# print(l9)
# l9.sort(reverse=True)
# print(l9)

# l10 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# l10.sort(key=lambda x: x**2)
# print(l10)

# l11 = ['hello', 'world', 'python', 'java', 'c++']
# l11.sort(key=lambda x: x[-1])
# print(l11)

# l12 = [-2, -1, 0, 1, 2]
# l13 = sorted(l12, key=lambda x: x**3 - 5, reverse=True)
# print(l12)
# print(l13)
