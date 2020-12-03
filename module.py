#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier module du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire :
    
"""


def readWord():
    wordDoc = open('liste_mot.txt')
   
    wordList = []
    for el in wordDoc :
        wordList.append( el.rstrip('\n') )
        
    wordDoc.close()
    wordList.sort()
    
    return(wordList)

print(readWord())