import csv
import sys
from PIL import Image, ImageOps
from os.path import splitext

def check_extension(file):
    if file in ['.jpg', '.jpeg', '.png']:
        return True
    return False

try:
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line argumnts")
    file1=splitext(sys.argv[1])
    file2=splitext(sys.argv[2])
    if check_extension(file1[1])==False:
        sys.exit("Invalid output")
    #if file1 not in [".jpg", ".jpeg", ".png"]:
     #   sys.exit("Invalid output")
    if file1[1].lower()!=file2[1].lower():
         sys.exit("Input and ouput have different extensions")
    #if ".jpg" or ".jpeg" or ".png" not in sys.argv[1] and sys.argv[2]:
        #sys.exit("Not a image file")

    image=Image.open(sys.argv[1])
    shirt=Image.open("shirt.png")
    size=shirt.size

    muppet=ImageOps.fit(image, size)

    muppet.paste(shirt,shirt)
    muppet.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("File does not exist")
