drink = input()
sugar = input()
quantity = int(input())


espresso_prices = {"Without": 0.90, "Normal": 1.00, "Extra": 1.20}
cappuccino_prices = {"Without": 1.00, "Normal": 1.20, "Extra": 1.60}
tea_prices = {"Without": 0.50, "Normal": 0.60, "Extra": 0.70}


if drink == "Espresso":
    drink_price = espresso_prices[sugar]
elif drink == "Cappuccino":
    drink_price = cappuccino_prices[sugar]
elif drink == "Tea":
    drink_price = tea_prices[sugar]


if sugar == "Without":
    drink_price *= 0.65

if drink == "Espresso" and quantity >= 5:
    drink_price *= 0.75


total_price = drink_price * quantity


if total_price > 15:
    total_price *= 0.8


print(f"You bought {quantity} cups of {drink} for {total_price:.2f} lv.")
