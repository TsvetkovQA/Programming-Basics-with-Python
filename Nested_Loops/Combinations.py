n = int(input())
count = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        x3 = n - x1 - x2
        if 0 <= x3 <= n:
            count += 1

print(f"{count}")
