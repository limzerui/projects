import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
        match=re.search(r"^([1-9]{1}[0-2]?)( |:([0-5][0-9]) )([A|P])M to ([1-9]{1}[0-2]?)( |:([0-5][0-9]) )([A|P])M$", s)
        if match:

            if match.group(4)=="P":
                hour=int(match.group(1))
                hour=hour+12
            else:
                hour=int(match.group(1))

            if match.group(8)=="P":
                hours=int(match.group(5))
                hours=hours+12
            else:
                hours=int(match.group(5))

            if match.group(2)==" ":
                minutes=00
            else:
                minutes=int(match.group(3))

            if match.group(6)==" ":
                minutess=00
            else:
                minutess=int(match.group(7))

            final=f"{hour:02}:{minutes:02} to {hours:02}:{minutess:02}"
        else:
            raise ValueError
        return final
        print("ValueError")





if __name__=="__main__":
    main()