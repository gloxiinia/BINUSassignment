#Ramp
'''
Problem -
Write a program that prompts the user to enter the Force and mass of the cart
Store the value of g as a ‘constant’ in your program) The program should then use the formula to calculate the angle of the ramp
Format your output to 1 decimal place
Note: The trigonometric functions in the math module returns the values in radians 
In addition to the arc sin function (asin), you will need to use the degrees function to convert the angle to degrees

Algorithm -
IMPORT math module
SET gravity = 9.8
PRINT request for 1st value
    'Enter the mass of the cart (in kg):'
PRINT request for 2nd value
    'Enter the force to push the cart (in N):'
CALCULATE the angle of the ramp with sin angle equals to 2nd value divided by (1st value times gravity)
CONVERT the angle of the ramp into degrees
PRINT 'The angle of the ramp is <angle of the ramp formatted to 1st decimal places>'

'''
import math
g = 9.8
m = float(input('Enter the mass of the cart (in kg):'))
f = float(input('Enter the force to push the cart (in N):'))


angle = math.degrees(math.asin(f / (m*g)))
print('The angle of the ramp is %.1f degrees' %angle)
