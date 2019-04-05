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
#IMPORTS#
import random

#VARIABLES#
alphabetLowerC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetUpperC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = [0,1,2,3,4,5,6,7,8,9]
puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]

#EXECUTION#
#Define lenght password
psLenght = random.randint(8,12)    
print("Length password:", psLenght)

#Define random items of password
Lower = alphabetLowerC[random.randint(0,25)]

Upper = alphabetUpperC[random.randint(0,25)]

Nmbr = number[random.randint(0,8)]

Punct = puncList[random.randint(0,14)]

#Define random tables, confirm that each table is used, create password
password = [Lower, Upper, Nmbr, Punct]

while len(password) < psLenght:
    master = random.randint(0,3)
    if master == 0:
        slave = alphabetLowerC
    elif master == 1:
        slave = alphabetUpperC
    elif master == 2:
        slave  = number
    elif master == 3:
        slave = puncList
    randomNum = random.randint(0, len(slave)-1)
    password.append(slave[randomNum])

#Shuffle tables
random.shuffle(password)
print(*password, sep="")