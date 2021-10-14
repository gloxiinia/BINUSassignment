#Windchill
'''
Problem -
Write a program that:
• asks the user to enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit
o Input validation: If the user enters a temperature not in range, use an if statement or while loop to ask them to re-enter the value
• asks the user to enter a windchill greater than 2mph
o Input validation: If the user enters a wind speed not in range, use an if statement or while loop to ask them to re-enter the value 
The program then calculates the wind-chill temperature using the formula above 
Format the output to 3 decimal places

Algorithm -
SET temperature = 0
WHILE TRUE THEN
    PRINT request for input
        'Enter the temperature in Fahrenheit:'
    IF value entered is lesser than 41 OR greater than -58 THEN
    ENDIF
    WHILE value entered is greater than 41 or less than -58 THE
    PRINT Temperature must be between -58F and 41F
    PRINT request for input
        'Please re-enter the temperature in Fahrenheit:'
    WHILE TRUE THEN
        PRINT request for input
            'Enter the wind speed miles per hour:'
        IF value entered is greater than or equal to 2 THEN
            CALCULATE windchill with windchill formula
            PRINT'The wind chill index is <windchill formatted to 3rd decimal places>"
        ENDIF
        WHILE value entered is less than 2 THEN
            PRINT 'Speed must be greater than or equal to 2'
            PRINT request for input
                'Please re-enter the wind speed miles per hour:'
        ELSE 
            CALCULATE windchill with windchill formula
            PRINT 'The wind chill index is <windchill formatted to 3rd decimal places>"
        ENDWHILE
    ENDWHILE
    
'''
temp = 0
while True :
    temp = float(input('Enter the temperature in Fahrenheit:'))
    if -58 > temp > 41:
        break
    while temp >= 41 or temp <= -58: 
        print('Temperature must be between -58F and 41F')
        temp = float(input('Please re-enter the temperature in Fahrenheit:'))
        
    while True:
        v = float(input('Enter the wind speed miles per hour:'))
        if v >= 2:
            wc = 35.74 + ((0.6215 * temp) - (35.75 *(v**0.16)) + (0.4275 * temp *(v**0.16)))
            print('The wind chill index is %.3f' %wc)
            break
        while v < 2:
            print('Speed must be greater than or equal to 2')
            v = float(input('Please re-enter the wind speed miles per hour:'))
        else:
            wc = 35.74 + ((0.6215 * temp) - (35.75 *(v**0.16)) + (0.4275 * temp *(v**0.16)))
            print('The wind chill index is %.3f' %wc)
        break  
    break        
        


