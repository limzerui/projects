def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x=len(s)
    if x<2 or x>6:
        return False
    if s[0] and s[1] in ['1','2','3','4','5','6','7','8','9','0']:
        return False
        #for? y in s?
    i=0
    while i<len(s):
        if s[i].isalpha()==False:
            if s[i] =='0':
                return False
            else:
                break
        i += 1

    for y in s:
        if y in ['.',' ', '!', '?']:
            return False


    return True



main()