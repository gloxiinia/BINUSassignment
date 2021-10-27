'''
The aspect ratio of an image describes the relationship between the width and height. 
Aspect ratios are usually expressed as two numbers separated by a colon that represent width and height respectively. 
Common aspect ratios in photography are 4:3, 3:2, and 16:9. 
An image that has an aspect ratio of x : y means that for every x inches of width you will have y inches of height no matter the size of the image 
(and, of course, you can use any unit of length, not just inches, and even abstract units such as pixels). 
Suppose you are writing a blog and you have an image that is m units wide and n units high but your blog 
only has space for an image that is z units wide (where z is less than m). 
Write a function called calc new height() that returns the height the image must be in order to preserve the aspect ratio 
(i.e., a height that will not distort the image). 
This function takes no arguments and prompts the user for the current width, the current height, and the desired new width. 
In addition to returning the new height, this function also prints the value. 
The new height is a float regardless of the types of the values the user entered.
'''
#Creates a new function for calculating the height of new aspect ratio
def calc_new_height():
    #Input validation for width
    while True:
    #Prompts user input for current img height, width and new desired width
        width_now = eval(input('Next, what\'s the current width of the image?'))
        height_now = eval(input('What\'s the current height of the image?'))
        new_width = eval(input('Okay, so what\'s the new width you want for the image?'))
        if new_width > width_now:
            print('Aw shucks, the new width\'s gotta be smaller than the current width :( \nPlease enter it again yeah?')
            continue
        else:
            break

    #Calculates the aspect ratio 
    asp_ratio = height_now/width_now
    #Calculates the new height and rounds it to the nearest whole number
    new_height = round(new_width*asp_ratio,0)

    #Calculates new height
    new_h = print('Alright, so the height you need for your image to NOT be distorted is', new_height)

    return new_h

calc_new_height()
    

