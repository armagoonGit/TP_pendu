#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier qui gere les mechaniques du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire : si la lettre n'est pas bon chance sur 8
    
"""

from module import addLettre, printGuesWord

def valideLettre(lettre):
    if len(lettre) > 1 or len(lettre) < 1:
        return( False )
    
    lettre = lettre.capitalize()
    oLettre = ord(lettre)
    
    if oLettre < ord('A') or oLettre > ord('Z'):
        return( False )
    return(lettre)

def askLettre():
    lettre = input("Veuiller choisir une lettre : ")
    while valideLettre(lettre) == False:
        lettre = input("Veuiller choisir une lettre valide : ")
    return( lettre )
        

def checkPresence(guesWord = "A____", word = "ARBRE",lettre = 'B') :
    if lettre in word :
        for i in range( len( word ) ):
            if word[i] == lettre:
                guesWord = addLettre(guesWord, lettre, i)
    else:
        print("la lettre n'est pas dans le mot")
        
    printGuesWord(guesWord)
    return(guesWord)
    
def genWordUnder(word):
    lenWord = len( word )
    guesWord = word[0] + '_'*(lenWord - 1)
    printGuesWord(guesWord)
    return(guesWord)

def stopGame(guesWord):
    if '_' in guesWord:
        return(False)
    return(True)

                

