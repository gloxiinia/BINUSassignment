import math

#nume and deno stand for numerator and denominator respectively.
nume = int(input('Enter a numerator (Value must be greater than 0):'))
while nume <= 0:
    print("The numerator's gotta be greater than 0")
    nume = int(input('Please re-enter a valid numerator:'))

deno = int(input('Enter a denominator (Value must be greater than 0):'))
while deno <= 0:
    print("The denominator's gotta be greater than 0")
    deno = int(input('Please re-enter a valid denominator:'))

#formula for gcd
gcd = math.gcd(nume, deno)

#reduction formulas
reduc1 = nume//gcd
reduc2 = deno//gcd

#formulas for mixed numbers
mix1 = nume//deno
mix2 = nume%deno
mix3 = reduc1%reduc2

if nume < deno:
    print(f'Whoa. {nume}/{deno} is a proper fraction, neat.')
    if gcd != 1:
        print(f'Good news! This proper fraction can be reduced to {reduc1}/{reduc2} ')
    else:
        print("Alas, this proper fraction can't be reduced.")
else:
    print(f'{nume}/{deno} be an improper fraction yo.')
    if gcd != 1:
        print(f"Hey, this improper fraction can be reduced to {reduc1}/{reduc2} y'know.")
        if mix2 != 0:
            print(f'The mixed number is {mix1} and {mix3}/{reduc2}')
        else:
            print(f"Oh! A whole number, and it's {mix1}")
    else:
        print("Aw, this improper fraction can't be reduced.")
        if mix2 != 0:
            print(f'The mixed number is {mix1} and {mix2}/{deno}')
        else:
            print(f"Cool. A whole number, and it's {mix1}")
        
    
    