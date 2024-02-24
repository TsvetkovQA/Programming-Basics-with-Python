destination = input()
while destination != "End":
    minimum_budget = float(input())
    saved_money = 0

    while saved_money < minimum_budget:
        money_saved = float(input())
        saved_money += money_saved

    print(f"Going to {destination}!")
    destination = input()
