student_name = input()
current_grade = 1
total_grade = 0
is_excluded = False
grade_counter = 0
while current_grade <= 12:
    grade = float(input())
    if grade >= 4:
        total_grade += grade
        current_grade += 1
    else:
        grade_counter += 1
        if grade_counter > 1:
            is_excluded = True
            break

if not is_excluded:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {current_grade} grade")
