#Slope of a line
'''
Problem - 
Write a program that prompts the user to enter the coordinates of two points (x1, y1) and (x2, y2) 
The program should calculate and display the slope of the line that connects the two points
Format your output to five decimal places

ALgorithm -
PRINT request for 1st value
    "Enter the x-coordinate for point 1:"
PRINT request for 2nd value
    "Enter the y-coordinate for point 1:"
PRINT request for 3rd value
    "Enter the x-coordinate for point 2:"
PRINT request for 4th value
    "Enter the y-coordinate for point 2:"
CALCULATE slope of the line with (1st value subtracted by 2nd value) divided by (3rd value subtracted by 4th value)
PRINT 'The slope for the line that connect points <first value, second value> and <third value, fourth value> is <slope of the line formatted to fifth decimal places>'
'''
x1 = float(input("Enter the x-coordinate for point 1:"))
y1 = float(input("Enter the y-coordinate for point 1:"))
x2 = float(input("Enter the x-coordinate for point 2:"))
y2 = float(input("Enter the y-coordinate for point 2:"))

m = (x1 - y1)/(x2 - y2)
print(f'The slope for the line that connect points {x1, y1} and {x2, y2} is %.5f' %  m)





