import math

human_count = int(input())
entrance_fee = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

all_tax = human_count * entrance_fee
all_sun_lounger = math.ceil(human_count * 0.75) * sun_lounger_price
umbrella_count = math.ceil(human_count / 2) * umbrella_price
all_money = all_tax + all_sun_lounger + umbrella_count
print(f'{all_money:.2f} lv.')
