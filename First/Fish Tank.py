length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_lt = volume / 1000
occupied_space = volume_lt * (percent / 100)
liters_needed = volume_lt - occupied_space
print(liters_needed)
