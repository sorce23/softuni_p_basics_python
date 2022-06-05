number_of_students = int(input())
top = 0
good = 0
average = 0
bad = 0
average_grade = 0
for count in range(number_of_students):
    grade = float(input())
    if grade >= 5:
        average_grade += grade
        top += 1
    elif 5 > grade >= 4:
        average_grade += grade
        good += 1
    elif 4 > grade >= 3:
        average_grade += grade
        average += 1
    elif 3 > grade:
        average_grade += grade
        bad += 1
average_grade = average_grade / number_of_students
top = top / number_of_students * 100
good = good / number_of_students * 100
average = average / number_of_students * 100
bad = bad / number_of_students * 100
print(f'Top students: {top:.2f}%')
print(f'Between 4.00 and 4.99: {good:.2f}%')
print(f'Between 3.00 and 3.99: {average:.2f}%')
print(f'Fail: {bad:.2f}%')
print(f'Average: {average_grade:.2f}')
