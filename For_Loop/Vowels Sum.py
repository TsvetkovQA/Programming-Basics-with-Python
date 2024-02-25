user_input = input()

vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
total_sum = 0

for char in user_input:
    lowercase_char = char.lower()
    if lowercase_char in vowels:
        total_sum += vowels[lowercase_char]

print(f"{total_sum}")
