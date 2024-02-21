num_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
total_tournaments_won = 0

for _ in range(num_tournaments):
    result = input()

    if result == "W":
        total_points += 2000
        total_tournaments_won += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

average_points = (total_points - starting_points) / num_tournaments

percentage_won = (total_tournaments_won / num_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{percentage_won:.2f}%")
