from datetime import date
import re
import sys
import inflect
p=inflect.engine()

def main():
    date_of_birth=input("Date of Birth:")
    try:
        year, month, day=check(date_of_birth)
    except:
        sys.exit("Invalid date")
    date_birth=date(int(year), int(month), int(day))
    date_today=date.today()
    diff=date_today - date_birth
    minutes=diff.days*24*60
    output=p.number_to_words(minutes, andword="")
    print(output.capitalize()+" minutes")

def check(date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date):
        year, month, day = date.split("-")
        return year, month, day

if __name__=="__main__":
    main()