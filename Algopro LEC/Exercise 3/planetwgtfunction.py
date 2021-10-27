'''
Write a function called calc weight on planet() that calculates your equivalent weight on another planet. 

This function takes two arguments: your weight on Earth in pounds and the surface gravity of the planet of interest with units m/s2.

Make the second argument optional and supply a default value of 23.1 m/s2 which is the approximate surface gravity of Jupiter 
(Earth’s suface gravity is approximately 9.8 m/s2).

To perform the conversion, use the equation: weight is equal to mass times surface gravity. 
Since your weight on Earth is given and you know the Earth’s surface gravity, have your function use this information to calculate your mass 
(it is fine if, at this point, the units of mass are a mix of Imperial and the MKS system). 
Then, use your mass and the given surface gravity to calculate your effective weight on the other planet.
'''

#Creates the function for calculating the weight on the desired planet
#Optional parameter of Jupiter's surface gravity (plnt_grv)
def calc_wgt_on_plnt(weight, plnt_grv = 23.1):
    #Mass caclulation
    mass = weight/9.8
    #Equation for weight on a planet
    wgt_plnt = print(mass * plnt_grv)
    return wgt_plnt

calc_wgt_on_plnt(120, 23.1)


