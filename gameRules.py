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
    """
    Verifie que le parametre est bien une lettre seul.
    Return1 : la lettre en majuscule 
    Return2 : False si le parametre est incorect
    """
    
    if len(lettre) > 1 or len(lettre) < 1:
        return( False )
    
    lettre = lettre.capitalize()
    oLettre = ord(lettre)
    
    if oLettre < ord('A') or oLettre > ord('Z'):
        return( False )
    return(lettre)

def askLettre():
    """
    Demande a l'utilisateur une lettre jusuqu'a se qu'elle soit valide
    return : la lettre valide en majuscule
    """
    
    lettre = input("Veuiller choisir une lettre : ")
    
    while valideLettre(lettre) == False:
        lettre = input("Veuiller choisir une lettre valide : ")
    
    return( lettre )   

def checkPresence(guesWord = "A____", word = "ARBRE",lettre = 'B') :
    """
    Verifie que la lettre est presente' dans le mot, la remplace si oui
    sinon affiche un message.
    Return : le mot a deviner avec ses nouvelle lettre si besoin
    """
    
    if lettre in word :
        for i in range( len( word ) ):
            if word[i] == lettre:
                guesWord = addLettre(guesWord, lettre, i)
    else:
        print("la lettre n'est pas dans le mot")
        
    printGuesWord(guesWord)
    return(guesWord)
    
def genWordUnder(word):
    """
    Genere un str de meme longeur que le parametre avec la premeire lettre 
    visible, les autre sont des _
    """
    
    lenWord = len( word )
    guesWord = word[0] + '_'*(lenWord - 1)
    printGuesWord(guesWord)
    return(guesWord)

def stopGame(guesWord):
    """
    Return false si le mot n'est pas encore devinr entierement
    Sinon return true
    """
    if '_' in guesWord:
        return(False)
    return(True)

def endGame(guesWord):
    """
    Verifie en fin de partie si le joueur a trouve le mot ou non
    """
    if stopGame(guesWord) == True :
        print("youplaOup bravo c'est gagner")
    else :
        print("desoler mais c'est perdu")
                

