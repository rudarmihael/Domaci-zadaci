shops = {
    "Maxi": {
        "Bread": 100,
        "Novine": 50
    },
    "Idea": {
        "Bread": 95,
        "Novine": 62
    },
    "Roda": {
        "Bread": 97,
        "Novine": 62
    },
    "FreeShop": {
        "Bread": 62
    },
    "Pijaca": {
        "Bread": 99
    }
}

# Ispisati prodavnicu koja ima najvisu cenu hleba => Maxi
highest_price = 0
highest_price_shop = "Neka"

bread_price = 0
bread_shops = 0

for shop_name, items in shops.items():
    if "Bread" in items:
        bread_price += items["Bread"]
        bread_shops += 1

        if highest_price < items['Bread']:
            highest_price = items['Bread']
            highest_price_shop = shop_name


average_bread_price = bread_price / bread_shops

print(average_bread_price)
print(highest_price, highest_price_shop)

