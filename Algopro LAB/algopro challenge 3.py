'''
input an integer value

if it's divisible by 11, print a
if it's divisible by 9, print b
if it's divisible by 7, print c
if it's divisible by 2, print d 
everything else print e


example cases
input: 63
output: bc

input: 22
output: ad

put it on your github repository.
'''
#v is the integer value the user puts in

v = int(input("Enter a value here:"))

if v % 11 == 0:
    print('a', end='')
if v % 9 == 0:
    print('b', end='')
if v & 7 == 0:
    print('c', end='')
if v % 2 == 0:
    print('d', end='')
if v % 11 > 0 and v % 9 > 0 and v % 7 > 0 and v % 2 > 0:
    print('there is a remainder :(')