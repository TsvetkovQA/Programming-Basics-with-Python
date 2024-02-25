total_amount = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    amount = float(command)

    if amount < 0:
        print("Invalid operation!")
        break

    total_amount += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {total_amount:.2f}")
