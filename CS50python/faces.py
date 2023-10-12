def main():
    x=input("")
    y=convert(x)
    print(y)

def convert(lol):
    new=lol.replace(":(", "🙁").replace(":)", "🙂")
    return new

main()


