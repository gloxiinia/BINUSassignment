'''
Write a function called convert temp() that takes no arguments. 
This function obtains a temperature in Fahrenheit from the user and uses two helper functions to convert this temperature to Celsius and Kelvin. 
Write a helper function called convert to celsius() that takes a single argument in Fahrenheit and returns the temperature in Celsius using the formula
Tc = 5/9(Tf-32)

where Tc is the temperature in Celsius and Tf is the temperature in Fahrenheit. 
Write another helper function called convert to kelvin() that takes a single argument in degrees Celsius and returns degrees 
Kelvin using the formula
Tk = Tc + 273.15

where Tk is the temperature in Kelvin. Use these two functions within your convert temp() function to 
display (i.e., print) the temperatures for the user. The convert temp() does not return anything
'''
#Creates a function which will convert a temperature in Fahrenheit to Celsius and Kelvin
def convert_temp():
    #Prompts user to input a temperature in Fahrenheit
    temp_f = eval(input('Enter the temperature you wanna convert (P.S. Make sure it\'s in Fahrenheit yeah?):'))

    #Creates a function which will convert a temperature in Fahrenheit to Celsius
    def convert2celsius(Fahrenheit = temp_f):
        global temp_c

        #Converts temperature in Fahrenheit to Celsius with formula
        temp_c = (5/9) * (Fahrenheit - 32)
        return temp_c

    #Calling the function
    convert2celsius()

    #Creates a function which will convert a temperature in Celsius to Kevin
    def convert2kelvin(Celsius = temp_c):
        global temp_k

        #Converts temperature in Celsius to Kelvin with formula
        temp_k = Celsius + 273.15
        return temp_k

    #Calling the function   
    convert2kelvin()
    
    #Prints calculations for user
    print(f'Chills, the temperature in Fahrenheit is:{temp_f}\nWhile the temperature in Celsius is:{temp_c}\nAnd the temperature in Kelvin is:{temp_k}')
        
convert_temp()


        

        



    

