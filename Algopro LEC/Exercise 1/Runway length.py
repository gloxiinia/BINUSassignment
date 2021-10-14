#Runway Length
'''
Problem - 
Write a program that prompts the user to enter the speed in meters per second (m/s) and the acceleration in meters 
per second squared (m/s2) 
The program should calculate and display the minimum runway length 
Format the result to four decimal places. (For this question, assume that all values entered are positive.)

Algorithm =
PRINT request for 1st value
	"Enter the plane's take off speed in meters per second:"
PRINT request for 2nd value
	"Enter the plane's acceleration in meters per second squared:"
IF 1st value and 2nd value are greater than 0 THEN
	CALCULATE the minimum runway length with (1st value squared) divided by (2 times the 2nd value)
	PRINT 'The minimum runway length needed for this airplane to take off is <minimum runway length formatted to 4th decimal place>'
ELSE
	PRINT 'Value entered must be positive :('
	ENDIF

'''

v = float(input("Enter the plane's take off speed in m/s:"))
a = float(input("Enter the plane's acceleration in m/s**2:"))

if v > 0 and a > 0:
    min_rw = v**2/(2*a)
    print('The minimum runway length needed for this airplane to take off is %.4f' % min_rw)
else:
    print('Value entered must be positive :(')
