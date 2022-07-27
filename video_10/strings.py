from os import system as sys
sys('clear')




# a = 'hello world media'
# print(a, end='\n\n')

# b = "hello world media"
# print(b, end='\n\n')


# c = '''
#         hello 
#         world 
#         media
#     '''
# print(c, end='\n\n')
    
# d = """
#         hello
#         world
#         media
#     """
# print(d, end='\n\n')


# e = "see 'main' file"
# print(e, end='\n\n')

# f = 'see "main" file'
# print(f, end='\n\n')

# g = "see \"main\" file"
# print(g, end='\n\n')




### indexing in python
#   'hello world media'
#    0123456789...
#       ...-4 -3 -2 -1
string = 'hello world media'

# print('first character of "hello world media": <', string[5], '>', sep='')
# print('last character of "hello world media": <', string[-1], '>', sep='')


### Slicing --> [start:stop:step]
# print('from index 0 to index 5: <', string[0:5], '>', sep='')
# print('from index 6 to end: <', string[6:], '>', sep='')
# print('from index 0 to index 5: <', string[:5], '>', sep='')
# print('from index 0 to end and step 2: <', string[::2], '>', sep='')
# print('from index -1 to end and step -6: <', string[-1:-6], '>', sep='')
# print('from index -1 to end and step -6: <', string[-1:-6:-1], '>', sep='')
# print('reverse of "hello world media": <', string[::-1], '>', sep='')





# print(len(string))