import math
import random
import time
import string
from wordlist import words

art = {0:"",1:"+---+",2:"+---+\n""|   O",3:"+---+\n""|   O\n""|  /|\\",4:" +---+\n""|   O\n""|  /|\\\n""|   |",5:"+---+\n""|   O\n""|  /|\\\n""|   |\n" "|  / \\",
       6:"+---+\n""|   O\n""|  /|\\\n""|   |\n" "|  / \\\n""========="}
words = ["reach","blind","guess","joint","piano","claim","stake","kneel","clash","sight","plant","brain","crime","craft","Koran",
         "ready","crack","pitch","mouth","thank","beard","dozen","knock","snail","lunch","bless","ample","trace","quiet","cable"]

game = True
playerinput = ""
mistakes = 0
chosen = random.choice(words)
print(chosen)
guesses = ["_","_","_","_","_"]

while game == True:
    holder = 0
    playerinput = input("Enter your letter: ")
    for i in range(len(chosen)):
        if chosen[i] == playerinput:
            guesses[i] = playerinput
        else:
            holder += 1
    for chars in guesses:
        print(chars, end=" ")
    if holder == 5:
        mistakes += 1

    print()
    print(art[mistakes])
    print(f"{mistakes} mistakes")
    if guesses.count("_") == 0:
        print("Congratulations! You win!")
        game = False
    if mistakes == 6:
        print("You lost!")
        game = False