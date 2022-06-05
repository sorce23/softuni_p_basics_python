student_name = input()
year = 1
average_grade = 0
fail = 0
while year <= 12:
    if fail > 1:
        break
    grades = float(input())
    if grades < 4:
        fail += 1
        continue
    average_grade += grades
    year += 1
if fail > 1:
    print(f'{student_name} has been excluded at {year} grade')
else:
    average = average_grade / 12
    print(f'{student_name} graduated. Average grade: {average:.2f}')
