import random
import sys

while True:
    try:
        level=int(input("Level:"))
        if level>0:
            break
    except:
        pass

x=random.randint(1, level)


while True:
    try:
        guess = int(input("Guess:"))
        if guess>0:
            if guess<x:
                print("Too small!")

            elif guess>x:
                print("Too big!")

            elif guess==x:
                print("Just right!")
                break
    except:
        pass


