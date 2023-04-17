from game import game
from words import random_word

def main():
    
    hidden = list('_' * len(random_word.strip()))
    chances = 0
    
    game(hidden, chances)
