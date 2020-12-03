#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier qui gere les mechaniques du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire :
    
"""

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
        

