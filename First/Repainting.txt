nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())
price_nylon = (nylon +2) * 1.5
price_paint = (paint * 1.1) * 14.5
price_thinner = thinner * 5
price_all_materials = price_nylon + price_paint + price_thinner + 0.40
money_for_working = (price_all_materials * 0.30) * working_hours
total_price = price_all_materials + money_for_working
print(total_price)
