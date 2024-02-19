chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegetarian_menu = vegetarian_menu * 8.15
all_price_menu = price_chicken_menu + price_fish_menu + price_vegetarian_menu
price_of_dessert = all_price_menu * 0.20
final_price = all_price_menu + price_of_dessert + 2.50
print(final_price)
