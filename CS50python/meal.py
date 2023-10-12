def main():
    a=input('Time: ')
    b=convert(a)
    if(b<=8 and b>=7):
        print ("breakfast time")
    if(b<=13 and b>=12):
        print("lunch time")
    if(b<=19 and b>=18):
        print('dinner time')
    else:
        print(' ')



def convert(time):
    hours, minutes = time.split(":")
    minutes =float(minutes)/60
    x=float(hours) + minutes
    return x


if __name__ == "__main__":
    main()