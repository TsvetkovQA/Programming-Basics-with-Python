days = int(input())
room_type = input()
review = input()

price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

total_price = price_per_night * (days - 1)

if days > 15:
    if room_type == "apartment":
        total_price = total_price - (total_price * 0.5)
    elif room_type == "president apartment":
        total_price = total_price - (total_price * 0.20)
elif 10 <= days <= 15:
    if room_type == "apartment":
        total_price = total_price - (total_price * 0.35)
    elif room_type == "president apartment":
        total_price = total_price - (total_price * 0.15)
elif days < 10:
    if room_type == "apartment":
        total_price = total_price - (total_price * 0.30)
    elif room_type == "president apartment":
        total_price = total_price - (total_price * 0.10)

if review == "positive":
    all_price = (total_price * 0.25) + total_price
elif review == "negative":
    all_price = total_price - (total_price * 0.10)

print(f"{all_price:.2f}")
