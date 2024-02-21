n = int(input())

max_num = int(input())
min_num = max_num

for i in range(2, n + 1):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
