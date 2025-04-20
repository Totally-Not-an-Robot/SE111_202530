
#if anyone sees this, I made this for my math class to calculate monthly loan repayments from their weird formula, didnt feel like finding my scientific calcualtor and typing it all in

from os import system, name

#------FUNCTIONS--------

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

aee = int(input("borrow amount: "))
bee = input("rate in percent x 100 [ex: 4.25% > 425]: ")
cee = input("years: ")

iee = (int(bee))/100/100/12     #double /100 due to not feeling like dealing with decimals on the input
print(iee)
xee = (int(cee))*12
print(xee)
ree_1 = (1 - (1 + iee)**-xee)/iee
print(ree_1)
ree_2 = aee/ree_1
print(ree_2)