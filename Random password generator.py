"""
---------Password Generator-------
Create a ps generator that has random outputs.
Spec:
    8 caracters min
    12 max
    1 Maj mini
    1 Ponct mini
    1 number mini
    must be totally random at each stage
    the only fct allowed to use is random
------------------------------------

"""
#VARIABLES#
alphabetLowerC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetUpperC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = [0,1,2,3,4,5,6,7,8,9]
puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
size8 = [0,1,2,3,4,5,6,7]
size9 = [0,1,2,3,4,5,6,7,8]
size10 = [0,1,2,3,4,5,6,7,8,9]
size11 = [0,1,2,3,4,5,6,7,8,9,10]
size12 = [0,1,2,3,4,5,6,7,8,9,10,11]

#EXECUTION#
import random

#Password lenght
psLenght = random.choice([size8,size9,size10,size11,size12])
for i, value in enumerate(psLenght):
    i = random.choice(number)
    print(i)

