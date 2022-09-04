from os import system
system('clear')




### why we need loops in programming
# l = [1, 1.1, 'hello', True, 1+2j,
#      'this world', 'this is a test', 'https://youtube.com/hello_world_media']
# 
# counter = 0
# if isinstance(l[0], str) and len(l[0]) > 5:
#     counter += 1
# if isinstance(l[1], str) and len(l[1]) > 5:
#     counter += 1
# if isinstance(l[2], str) and len(l[2]) > 5:
#     counter += 1
# if isinstance(l[3], str) and len(l[3]) > 5:
#     counter += 1
# if isinstance(l[4], str) and len(l[4]) > 5:
#     counter += 1
# ...



### while loop
# l1 = [1, 1.1, 'hello', True, 1+2j,
#      'this world', 'this is a test', 'https://youtube.com/hello_world_media']

# counter = 0
# i = 0
# while i < len(l1):
#     if isinstance(l1[i], str) and len(l1[i]) > 5:
#         counter += 1
#     i += 1

# print(counter)


### flow control
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## break
# i = 0
# while i < len(l2):
#     if l2[i] == 5:
#         break
#     print(l2[i])
#     i += 1
# print('end of the loop')

## continue
# i = 0  
# while i < len(l2):
#     if l2[i] < 5:
#         i += 1
#         continue
#     print(l2[i])
#     i += 1
# print('end of the loop')


### loop run time steps
# '''
#     l = [1, 2, ..., 10]
#     i = 0
#     while i < len(l):
#         print(l[i])
#         i += 1
        
#     runtime steps:
#         step.1: check while condition
#         step.2: execute the loop body
#         step.3: increment i (usually)
#         step.4: go to step.1
# '''
# # i = 0
# # while i < -1:
# #     print(i)
# #     i += 1


# ### else for while loop
# l3 = [1, 2, 3, 4, 5, 6, 7]
# i = 0
# while i < len(l3):
#     if l3[i] == 5:
#         i += 1
#         continue
#         # break
#     print(f'l3[{i}] = {l3[i]}')
#     i += 1
# else:
#     # todo: do something
#     print('end of the loop')


### ifinite loop
# while True:
#     print('hello world', end=' ')