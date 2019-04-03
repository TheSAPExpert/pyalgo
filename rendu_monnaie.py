"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to rest of int div
Use input() function to a user entry
"""
panier = 700
somme = 1000
aRendre= somme - panier

#Got 100
nbBillet100 = aRendre // 100
left100 = aRendre % 100
#Next got 50
nbBillet50 = left100 // 50
left50 = left100 % 50
#Next got 10
nbBillet10 = left50 // 10
left10 = left50 % 10
#Next got coins of 2
nbCoins = left10 // 2
leftCoins = left10 % 2
#This is the End Friends
print("Je vous dois: .... \n", nbBillet100, "x100/n", nbBillet50, "x50/n", nbBillet10, "x10/n", nbCoins, "x2/n", leftCoins, "/n")