# -*- coding: utf-8 -*-
"""

que fait : fichier pricipal du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire : genre les mots avec accent mais si y en aps dans la liste mot
                    AUCUN probleme

"""

from module import getWord
from gameRules import askLettre, genWordUnder, checkPresence, stopGame, endGame

def main():
    nbTurn = 0
    nbError = 0
    word = getWord()
    lettreList = [ word[0] ]
    guesWord = genWordUnder(word)
    
    while stopGame(guesWord) == False and nbError <= 8 :
        lettre = askLettre(lettreList)
        guesWord,error = checkPresence(guesWord, word, lettre)
        
        nbTurn += 1
        nbError += error
        
        
    
    endGame(guesWord, nbTurn, word)
    replay = input("Voulez vous rejouez une partie ? y/n ").capitalize()
    if replay == 'Y':
        main()
    

main()