from os import system
from string import Template
system('clear')




### why we need string formatting
# a = int(input())
# print('2 x ' + str(a) + ' = ' + str(2*a) + ' and 3 x ' + str(a) + ' = ' + str(3*a))




### no.1 way of string formatting
# a = int(input())
# b = float(input())
# print('2 x %s = %s and 3 x %s = %s' % (a, 2*a, a, 3*a))
# print('a: 2 x %d = %d and 3 x %d = %d' % (a, 2*a, a, 3*a))
# print('b: 2 x %.1f = <%5.1f> and 3 x %.1f = %.1f' % (b, 2*b, b, 3*b))
'''
    format of % operator: %[flags][width][.precision]type
    %s - string (or any object with a string representation)
    %d - integer (or any object with a numeric representation)
    %f - floating point number (or any object with a numeric representation)
    %b - binary representation (or any object with a numeric representation)
    %o - octal representation (or any object with a numeric representation)
    %x - hexadecimal representation (or any object with a numeric representation)
    %e - exponential notation (or any object with a numeric representation)
    %% - percent sign
'''



### no.2 way of string formatting
# a = int(input())
# b = float(input())
# # print('2 x {} = {} and 3 x {} = {}'.format(a, 2*a, a, 3*a))
# print('a: 2 x {:d} = {:d} and 3 x {:d} = {:,}'.format(a, 2*a, a, 3*a))
# print('b: 2 x {:.1f} = <{:5.1f}> and 3 x {:.1f} = {:.1f}'.format(b, 2*b, b, 3*b))

# print('{2} {2} {0} {1}'.format('a', 'b', 'c'))
# print('{a} {a} {b} {c}'.format(a='a', b='b', c='c'))



### no.3 way of string formatting
# a = int(input())
# b = float(input())
# print(f'a: 2 x {a:d} = {2*a:d} and 3 x {a:d} = {3*a:,}')
# print(f'b: 2 x {b:.1f} = <{2*b:5.1f}> and 3 x {b:.1f} = {3*b:.1f}')
# print(f'is 3 > 5? {3 > 5}')



### no.4 way of string formatting
a = int(input())
b = float(input())

t = Template('a: 2 x $mamad = $b and 3 x $a = $c')
print(t.substitute(mamad=a, a=a, b=2*a, c=3*a))

tf = Template('b: 2 x $mamad = <$b> and 3 x $a = $c')
print(tf.substitute(mamad=b, a=b, b=2*b, c=3*b))
