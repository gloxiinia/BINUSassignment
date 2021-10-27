'''
Write a function called num atoms() that calculates how many atoms are in n grams of an element given its atomic weight. 
This function should take two parameters: 
the amount of the element in grams and an optional argument representing the atomic weight of the element. 
The atomic weight of any particular element can be found on a periodic table but 
make the default value for the optional argument the atomic weight of gold (Au) 196.97 with units in grams/mole. 

A mole is a unit of measurement that is commonly used in chemistry to express an amount of a substance. 
Avogadro’s number is a constant, 6:022_1023 atoms/mole, that can be used to find the number of atoms in a given sample. 
Use Avogadro’s number, the atomic weight, and the amount of the element in grams to find the number of atoms present in the 
sample. 
Your function should return this value.
Avogadro's number = 6.02214076e+23 mol^-1 = 6.02214076e+23
Number of atoms = Avogadro's number * number of moles
Atomic weight = amount of e in grams/number of moles
Number of moles = amount of e in grams/atomic weight
'''
#Creates a function to calculate the number of atoms in a substance
def num_atoms(elem_gr, atom_wgt = 196.97):
    #Calculates number of moles
    num_moles = elem_gr/atom_wgt
    #Calculates number of atoms with Avogadro's number
    numb_atoms = print(6.02214076e+23 * num_moles)
    return numb_atoms

num_atoms(10, 12.001)
num_atoms(10, 1.008)

