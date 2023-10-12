import sys
import requests

if len(sys.argv) == 2:
    try:
        n=float(sys.argv[1])
    except:
        print("please input how many uw to buy")
        sys.exit(1)
else:
    sys.exit(1)



try:

    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    price=(o["bpi"]["USD"]["rate_float"])
except requests.RequestException:
    sys.exit

price=price*n
print(f"${price:,.4f}")


