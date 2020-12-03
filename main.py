# -*- coding: utf-8 -*-
"""

que fait : fichier pricipal du projet pendu sans interface
qui : FOËX Vick 
quand : 3/12/2020
que reste a faire :

"""

from module import getWord
from gameRules import askLettre, genWordUnder, checkPresence, stopGame

def main():
    word = getWord()
    guesWord = genWordUnder(word)
    
    while stopGame(guesWord) == False :
        lettre = askLettre()
        guesWord = checkPresence(guesWord, word, lettre)
    

main()