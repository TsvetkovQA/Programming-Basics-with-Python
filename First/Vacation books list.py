total_pages_count = int(input())
pages_per_hour = int(input())
days = int(input())
total_hours = total_pages_count // pages_per_hour
hour_per_day = total_hours // days
print(hour_per_day)
