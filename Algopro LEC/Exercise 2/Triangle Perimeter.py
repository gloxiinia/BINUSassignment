#Triangle Perimeter
'''
Problem -
Write a program that reads the three edges of a triangle and computes the perimeter if the input is valid 
The input is valid if the sum of every pair of two edges is greater than the remaining edge 
Otherwise (i.e. else) print a message stating that the input is invalid and the perimeter cannot be calculated
(Note: This question does NOT require further input validation.)

Algorithm -
PRINT request for 1st value
    'Enter length of edge 1:'
PRINT request for 2nd value
    'Enter length of edge 2:'
PRINT request for 3rd value:
    'Enter length of edge 3:'
IF 1st value + 2nd value is greater than 3rd value and 1st value + 3rd value is greater than 2nd value and 2nd value + 3rd value is greater than 1st value THEN
    PRINT 'Perimeter = <1st value + 2nd value + 3rd value>'
ELSE
    PRINT 'Input is invalid, unable to calculate :('
'''

e1 = float(input('Enter length of edge 1:'))
e2 = float(input('Enter length of edge 2:'))
e3 = float(input('Enter length of edge 3:'))
if e1+e2 > e3 and e1+e3 > e2 and e2+e3 > e1:
    print('Perimeter',e1+e2+e3, sep=' = ')
else:
    print('Input is invalid, unable to calculate :(')