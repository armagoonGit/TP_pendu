#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier module du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire :
    
"""

from random import randint

def readWord():
    wordDoc = open('liste_mot.txt')
   
    wordList = []
    for el in wordDoc :
        wordList.append( el.rstrip('\n') )
        
    wordDoc.close()
    wordList.sort()
    
    return(wordList)

def sortList(wordList):
    sieze = {}

    for el in wordList :
        lenEl = str( len( el ) )
        
        if lenEl in sieze: 
            sieze[ lenEl ].append( el )
        else:
            sieze[ lenEl ] = [el]
            
    key =sorted( list( sieze.keys() ) )
    wordList = []
    for k in key:
        wordList += sieze[k]
    
    print(wordList)


    


def pickWord(wordList):
    rand = randint(0, len(wordList) - 1 )
    print (rand, wordList[rand])
    

sortList(readWord())
    