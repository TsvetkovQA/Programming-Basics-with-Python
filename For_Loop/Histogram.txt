n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

p1 = p2 = p3 = p4 = p5 = 0

for num in numbers:
    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    else:
        p5 += 1

total = p1 + p2 + p3 + p4 + p5

print(f"{(p1 / total * 100):.2f}%")
print(f"{(p2 / total * 100):.2f}%")
print(f"{(p3 / total * 100):.2f}%")
print(f"{(p4 / total * 100):.2f}%")
print(f"{(p5 / total * 100):.2f}%")
