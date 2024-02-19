deposit_amout = float(input())
mounts = int(input())
annual_rate = float(input())
per_year = deposit_amout * (annual_rate/100)
per_mount = per_year / 12
total_sum = deposit_amout + (mounts * per_mount)
print(total_sum)
