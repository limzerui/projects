import re
import sys
def main():
    print(count(input("Text: ")))

def count(s):
    match=re.findall(r"\bum\b", s, re.IGNORECASE)
    number=len(match)
    return number

if __name__=="__main__":
    main()