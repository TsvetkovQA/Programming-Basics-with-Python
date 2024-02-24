start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combinations_found = False
combination_count = 0

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        combination_count += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_count} ({num1} + {num2} = {magic_number})")
            combinations_found = True
            break
    if combinations_found:
        break

if not combinations_found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
