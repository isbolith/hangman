# -*- coding: utf-8 -*-
"""
Hangman
"""

import random
import os

def run():
    IMAGES = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========''']
    
    
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP",
        "BASIC"
    ]
    
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    intentos = 6
    digitadas=[]
    
    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[intentos])
        print("Letras digitadas: ")
        for i in digitadas:    
            print(i, end=" ")
        letter = input("Elige una letra: ").upper()
        digitadas.append(letter)
        
        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
                
        if not found:
            intentos -= 1
        
        if "_" not in spaces:
            os.system("clear")
            print("\nGanaste")
            break
            
        if intentos == 0:
            os.system("clear")
            print("\nPerdiste")
            break

if __name__ == '__main__':
    run()