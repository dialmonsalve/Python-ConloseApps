

from hangman import hangman
from words import random_word

def game(hidden_word:str, chances:int):
    while chances < 7:

        hangman(chances)
        print("".join(hidden_word),'\n')
        
        if chances < 6:
            selected_letter = input('Escriba una letra: ').lower()

        if selected_letter in random_word:            
            for i in range(0, len(hidden_word)+1):
                if selected_letter == random_word[i]:
                    hidden_word[i-1]=selected_letter
        else:
            chances += 1

        if not '_' in hidden_word:
            break
            
    if chances == 6 or '_' in hidden_word:
        print('\n\n\n\n======YOU LOSE======')
    else:
        print('\n\n\n\n======YOU WIN======')

    hangman(chances)
    print('\nLa palabra es:',random_word.upper(),'\n')