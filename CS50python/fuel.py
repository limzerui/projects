while True:
    fuel = input('Fraction:')
    try:
        x, y=fuel.split("/")
        x = int(x)
        y = int(y)
        f = x/y
        if f<=1:
            break
    except (ValueError, ZeroDivisionError):
            pass
p = round(f*100)

if p<=1:
    print('E')
elif p>=99:
    print('F')

else:
    print(f"{p}%")






