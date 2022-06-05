hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
total_minutes_of_exam = (hour_of_exam * 60) + minutes_of_exam
total_minutes_of_arrival = (hour_of_arrival * 60) + minutes_of_arrival
difference = abs(total_minutes_of_exam - total_minutes_of_arrival)
hour = difference // 60
minutes = difference % 60
if total_minutes_of_arrival == total_minutes_of_exam:
    print('On time')
elif total_minutes_of_arrival < total_minutes_of_exam:
    if difference <= 30:
        print('On time')
        print(f'{minutes} minutes before the start')
    elif 30 < difference <= 59:
        print('Early')
        print(f'{difference} minutes before the start')
    else:
        print('Early')
        print(f'{hour}:{minutes:02d} hours before the start')
elif total_minutes_of_arrival > total_minutes_of_exam:
    print('Late')
    if difference < 60:
        print(f'{difference} minutes after the start')
    else:
        print(f'{hour}:{minutes:02d} hours after the start')
