poor_grades = int(input())
task_number = 0
poor_grades_counter = 0
average_grades = 0
last_task = ''
task_name = input()
is_failed = False
while task_name != 'Enough':
    grades = int(input())
    task_number += 1
    average_grades += grades
    last_task = task_name
    if grades <= 4:
        poor_grades_counter += 1
    if poor_grades_counter == poor_grades:
        is_failed = True
        break
    task_name = input()
average_grades = average_grades / task_number
if is_failed:
    print(f'You need a break, {poor_grades} poor grades.')
else:
    print(f'Average score: {average_grades:.2f}')
    print(f'Number of problems: {task_number}')
    print(f'Last problem: {last_task}')
