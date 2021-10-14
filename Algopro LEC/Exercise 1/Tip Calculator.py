#Tip Calculator
'''
Problem -
Write a program that reads the subtotal and gratuity rate 
The program then calculates and gratuity as a dollar amount, followed by the total amount, and displays all information in dollars
Your code should include currency formatting (i.e., use the $ in your output, include comma separation and format the result to 2 decimal places.)

Algorithm -
PRINT request for 1st value
    "Enter subtotal here:"
PRINT request for 2nd value
    "Enter tip amount (as a %)"
CALCULATE tip amount with 1st value times (2nd value divided by 100)
CALCULATE total amount by the sum of tip amount and 1st value
PRINT "Subtotal: <1st value formatted in dollars and 2nd decimal places with comma separation>"
PRINT "Tip: <tip amount formatted in dollars and 2nd decimal places with comma separation>"
PRINT "Total: <total amount formatted in dollars and 2nd decimal places with comma separation>"
'''

subtotal = float(input("Enter subtotal here:"))
tip = float(input("Enter tip amount (as a %):"))

tipr = subtotal*(tip/100)
total = tipr + subtotal

print("Subtotal: ${:,.2f}".format(subtotal))
print("Tip: ${:,.2f}".format(tipr))
print("Total: ${:,.2f}".format(total))
