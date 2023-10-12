eqn=input('Expression:')

x, y, z = eqn.split(' ')

x=int(x)

z=int(z)

if y=='+':
    results = x + z
if y=='-':
    results = x - z
if y=='*':
    results = x * z
if y=='/':
    results = x / z

results = float(results)


print(round(results, 1))
