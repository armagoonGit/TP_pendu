#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier qui gere score du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire : 
    
"""




def readWord():
    
    scoreDoc = open('score.txt',"r")
   
    scoreList = []
    for el in scoreDoc :
        
        scoreList.append( el.rstrip('\n').split(':') )
        
    scoreDoc.close() 
    return(scoreList)
    
def addScore(word, score):
    scoreList = readWord()
    scored = False
    
    
    scoreDoc = open('score.txt',"w")
   
    for el in scoreList:

        if el[0] == word :
            scored = True
            if score < int( el[1] )  :
                toWrite = str( score )
                print( "Nouveau score pour " + word + ": " + str( score )  )
            else:
                print( "Score a abatre pour " + word + ": " + el[1]  )
                toWrite = el[1]

        else :
            toWrite = el[1]
        scoreDoc.write(el[0] + ':' + toWrite + '\n' )
        
    if scored == False :
        print( "Nouveau score pour " + word + ": " + str( score )  )
        scoreDoc.write(word + ':' + str(score) + '\n' )
               
    scoreDoc.close() 
    
