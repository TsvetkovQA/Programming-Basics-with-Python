city = input()
sales_volume = float(input())

if sales_volume >= 0:
    commission = 0.0

    if city == "Sofia":
        if sales_volume <= 500:
            commission = 0.05 * sales_volume
        elif sales_volume <= 1000:
            commission = 0.07 * sales_volume
        elif sales_volume <= 10000:
            commission = 0.08 * sales_volume
        else:
            commission = 0.12 * sales_volume
    elif city == "Varna":
        if sales_volume <= 500:
            commission = 0.045 * sales_volume
        elif sales_volume <= 1000:
            commission = 0.075 * sales_volume
        elif sales_volume <= 10000:
            commission = 0.10 * sales_volume
        else:
            commission = 0.13 * sales_volume
    elif city == "Plovdiv":
        if sales_volume <= 500:
            commission = 0.055 * sales_volume
        elif sales_volume <= 1000:
            commission = 0.08 * sales_volume
        elif sales_volume <= 10000:
            commission = 0.12 * sales_volume
        else:
            commission = 0.145 * sales_volume
    else:
        print("error")

    if commission != 0.0:
        print("{:.2f}".format(commission))
else:
    print("error")
