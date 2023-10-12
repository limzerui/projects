from pyfiglet import Figlet
import random
from sys import argv
from sys import exit

figlet=Figlet()
x=figlet.getFonts()

if len(argv) ==1:
    random_format=random.choice(x)
    figlet.setFont(font=random_format)
    text=input("Input:")
    print(figlet.renderText(text))

elif len(argv) ==3 and (argv[1]=="-f" or argv[1]=="--font"):
    figlet.setFont(font=argv[2])
    text=input("Input:")
    print(figlet.renderText(text))
else:
    print("Invalid usage")
    exit



