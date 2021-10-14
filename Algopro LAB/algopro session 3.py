'''
while is similar to if, but it continues to run forever until proven false
you have to be careful with while and it'll take up your memeory and crash the computer

range is basically an easier way to make a list

think of everything as a variable

for loops goes through each element inside a list

under normal circumstances
a = 1
b = a
print(b)

1

but with lists, objects, etc
a = [1]
b = a -> you have to specify list(a) so it will have a seperate 'address' to 'link' to
b[0] = 21
print (a)
print (b)
21
21


'''
a = [1, 3, 5, 6]
b = list(a)
b[0] = 21
print(a)
print(b)