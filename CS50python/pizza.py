import csv
import sys
from tabulate import tabulate

try:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line argumnts")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a Python file")
    with open(sys.argv[1], "r") as file:
        reader=csv.DictReader(file)
        print(tabulate(reader, tablefmt="grid"))
        #print(reader)

    #with open(sys.argv[1], "r") as file:
       # line=file.readlines()
       # for x in line:
            #x.lstrip().rstrip()
            #print(x)
          #  if x.lstrip().rstrip().startswith("#")==False and x.startswith("\n")==False:

except FileNotFoundError:
    sys.exit("File does not exist")
