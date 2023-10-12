menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
x=int(0)
while True:

    try:
        item = input("Item:").title()

        if item in menu:
            price=menu.get(item)
            x=x+float(price)
            print("Price:$",end="")
            print("{:.2f}".format(x))

    except EOFError:
        print()
        break
    except KeyError:
        print("Keyerror")