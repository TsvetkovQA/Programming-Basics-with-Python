total_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_climbers = 0

for _ in range(total_groups):
    climbers_in_group = int(input())
    total_climbers += climbers_in_group

    if climbers_in_group <= 5:
        musala_count += climbers_in_group
    elif 6 <= climbers_in_group <= 12:
        monblan_count += climbers_in_group
    elif 13 <= climbers_in_group <= 25:
        kilimanjaro_count += climbers_in_group
    elif 26 <= climbers_in_group <= 40:
        k2_count += climbers_in_group
    else:
        everest_count += climbers_in_group

musala_percent = (musala_count / total_climbers) * 100
monblan_percent = (monblan_count / total_climbers) * 100
kilimanjaro_percent = (kilimanjaro_count / total_climbers) * 100
k2_percent = (k2_count / total_climbers) * 100
everest_percent = (everest_count / total_climbers) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
