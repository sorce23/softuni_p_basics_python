number_of_jury = int(input())
total_average = 0
presentation_counter = 0
presentation_is_finish = False
while not presentation_is_finish:
    presentation_name = input()
    grades = 0
    average_grade = 0
    if presentation_name == 'Finish':
        presentation_is_finish = True
        break
    presentation_counter += 1
    for count in range(number_of_jury):
        grade = float(input())
        grades += grade
    average_grade = grades / number_of_jury
    total_average += average_grade
    print(f'{presentation_name} - {average_grade:.2f}.')
if presentation_is_finish:
    total_average /= presentation_counter
    print(f"Student's final assessment is {total_average:.2f}.")
