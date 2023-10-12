
import sys

try:
    a=0
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line argumnts")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    with open(sys.argv[1], "r") as file:
        line=file.readlines()
        for x in line:
            #x.lstrip().rstrip()
            #print(x)
            if x.lstrip().rstrip().startswith("#")==False and x.startswith("\n")==False:
                a+=1

        #for line in file:
            #code.append(line.rstrip().lstrip())
    #print(code)
    #for i in code:
        #if i.startswith("#")==False and i.startswith("")==False:
          #  a+=1
    print(a)
except FileNotFoundError:
    sys.exit("File does not exist")
