'''
Software Sales

Problem -
Write a program that asks the user to enter the number of packages purchased
The program should then display the amount of the discount (if any) and the total of the purchase after the discount 
Use appropriate formatting to display currency and percentages in your output

Algorithm -
PRINT request for input
    'Enter the number of packages purchased:'
IF value input is equal to or greater than 10 AND less than 20 THEN
    SET discount value as 10%
ELIF value input is euqal to or greater than 20 AND less than 50 THEN
    SET discount value as 20%
ELIF value input is equal to or greater than 50 AND less than 100 THEN
    SET discount value as 30%
ELIF value input is equal to or greater than 100 THEN
    SET discount value as 40%
ELSE THEN
    SET discount value as 0
CALCULATE discount amount in dollars
CALCULATE total amount after discount
PRINT 'Discount Amount @ 0% : <discount amount formatted in dollars>'
PRINT 'Total Amount : <total amount after discount>'

'''
numspack = int(input('Enter the number of packages purchased:'))
if  20 > numspack >= 10:
    disc = 0.10
elif 50 > numspack >= 20:
    disc = 0.20
elif 100 > numspack >= 50:
    disc = 0.30
elif numspack >= 100:
    disc = 0.50
else:
    disc = 0

discdol = 99 * numspack * disc
total = (99 * numspack) - discdol

print('Discount Amount @ {:.0%}:'.format(disc),'${:.2f}'.format(discdol))
print('Total Amount: ${:.2f}'.format(total))