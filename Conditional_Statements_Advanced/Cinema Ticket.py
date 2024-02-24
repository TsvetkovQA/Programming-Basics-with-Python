day = input()
if day == "Monday" or day == "Friday" or day == "Tuesday":
    ticket_price = 12
    print(ticket_price)
elif day == "Wednesday" or day == "Thursday":
    ticket_price = 14
    print(ticket_price)
elif day == "Saturday" or day == "Sunday":
    ticket_price = 16
    print(ticket_price)

