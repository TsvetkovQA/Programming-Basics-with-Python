max_number = None

while True:
    number = input()

    if number == "Stop":
        break

    number = int(number)

    if max_number is None or number > max_number:
        max_number = number

if max_number is not None:
    print(max_number)
