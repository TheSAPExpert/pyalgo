"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use / to get an integer division
Use % to rest of int div
Use input() function to a user entry
"""

#Accept an amount entry
customerSomme = input("Somme en entreé : ")
somme = int(customerSomme)
#Got 100
nbBillet100 = somme / 100
left100 = somme % 100

if left100 > 0:
   #Next got 50
   nbBillet50 = somme / 50
   left50 = somme % 50

   #Next got 10
   nbBillet10 = somme / 10
   left10 = somme % 10

   #Next got coins of 2
   nbCoins = somme / 2
   leftCoins = somme % 2#This is the End Friends

print("And the result is.... \n", nbBillet100, "x100/n", nbBillet50, "x50/n", nbBillet10, "x10/n", nbCoins, "x2/n", nbleftCoins, "/n")