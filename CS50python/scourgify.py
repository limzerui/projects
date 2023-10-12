import csv
import sys

try:
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line argumnts")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a Python file")

    with open(sys.argv[2], "a") as file:
        with open(sys.argv[1]) as files:
            writer=csv.DictWriter(file, fieldnames=["first", "last", "house"])
            reader=csv.DictReader(files)
            for row in reader:
                first, last=row["name"].split(", ")
                house=row["house"]
                writer.writerow({"first":first, "last":last, "house":house})



except FileNotFoundError:
    sys.exit("File does not exist")
