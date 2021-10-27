'''
Write a function called convert to days() that takes no parameters. 
Have your function prompt the user to input numbers of hours, minutes, and seconds. 
Write a helper function called get days() that uses these values and converts them to days in float form (fractions of a day are allowed). 
get days() should return the number of days. 
Use this helper function within the convert to days() function to display the numbers of days to the user. 
The built-in function round() takes two arguments: a number and an integer indicating the desired precision (i.e., the desired number of digits beyond the decimal point). 
Use this function to round the number of days four digits after the decimal point.
'''
#Creates a function that prompts user input for hours, minutes and seconds
def conv2days():
    hours = float(input('Enter the number of hours pleaseee:'))
    mins = float(input('Now enter the minutesss:'))
    sec = float(input('Finally, enter the secondsss:'))
    #Creates a function that converts the values input into days and returns it
    def getdays():
        new_h = (hours/24)
        new_m = (mins/1440)
        new_s = (sec/86400)
        numdays = round(new_h + new_m + new_s, 4)
        return numdays
    print('And the number of days isss', getdays()) 
conv2days()

        

