string = input("input: ")
print("Output: ", end="")
for x in string:
    if not x.lower() in ['a','e','i','o','u']:
        print(x, end="")

print()