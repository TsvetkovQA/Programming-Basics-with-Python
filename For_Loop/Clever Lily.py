age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys_count = 0
money_gift = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += money_gift - 1
        money_gift += 10
    else:
        toys_count += 1

total_money = money + (toys_count * toy_price)

if total_money >= washing_machine_price:
    remaining_money = total_money - washing_machine_price
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = washing_machine_price - total_money
    print(f"No! {needed_money:.2f}")

      
