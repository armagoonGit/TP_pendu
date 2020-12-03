# -*- coding: utf-8 -*-
"""

que fait : fichier pricipal du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire :

"""

from module import getWord
from gameRules import askLettre, genWordUnder, checkPresence, stopGame, endGame

def main():
    nbTurn = 0
    word = getWord()
    guesWord = genWordUnder(word)
    
    while stopGame(guesWord) == False and nbTurn <= 8 :
        lettre = askLettre()
        guesWord = checkPresence(guesWord, word, lettre)
        
        nbTurn += 1
    endGame(guesWord)
    
    

main()