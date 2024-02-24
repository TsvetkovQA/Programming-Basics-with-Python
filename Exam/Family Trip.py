budget = float(input())
number_of_nights = int(input())
overnight_price = float(input())
additional_costs = int(input())

if number_of_nights > 7:
    overnight_price *= 0.95

total_night = number_of_nights * overnight_price
bills = additional_costs * budget / 100
total = total_night + bills

if budget >= total:
    money_left = budget - total
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    money_needed = total - budget
    print(f'{money_needed:.2f} leva needed.')
