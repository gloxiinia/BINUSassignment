#Area of Hexagon
'''
Problem -
Write a program that prompts the user to enter the side of a hexagon and displays its area
Assume that the side entered is positive
Format the result to three decimal places
Use the functions pow and sqrt from the math module to express the formula accurately

Algorithm -
IMPORT math module
PRINT request for 1st value
    'Enter the side length of the hexagon:'
CALCULATE the area of the hexagon with the formula ((3 times the square root of 3) divided by 2) times the 1st value squared
PRINT 'The area of a hexagon with a side length of 5 is <area of the hexagon formatted to 3rd decimal places>'

'''
import math
side = float(input('Enter the side length of the hexagon:'))

a = ((3 * math. sqrt(3)/2)) * math. pow(side, 2)
print('The area of a hexagon with a side length of 5 is %.3f' % a)