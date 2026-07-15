import math
import random
import time
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(chars)
print(key)

encryptedword = []


while True:
    chose = input("1. Encrypt\n2. Decrypt\n3. Exit\n ")
    if chose == "1":
        word = input("Type word to encrypt: ")
        for i in range(len(word)):
            index = chars.index(word[i])
            encryptedword.append(key[index])
        for char in encryptedword:
            print(char, end="")
        print()
        encryptedword.clear()

    elif chose == "2":
        word = input("Type word to decrypt: ")
        for i in range(len(word)):
            index = key.index(word[i])
            encryptedword.append(chars[index])
        for char in encryptedword:
            print(char, end="")
        print()
        encryptedword.clear()
    elif chose == "3":
        break
    else:
        print("Invalid input")

