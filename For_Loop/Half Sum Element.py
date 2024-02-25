n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

total_sum = sum(numbers)
max_number = max(numbers)

found = False

for num in numbers:
    if num == total_sum - num:
        print("Yes")
        print("Sum =", num)
        found = True
        break

if not found:
    diff = abs(total_sum - 2 * max_number)
    print("No")
    print("Diff =", diff)
