free_days = int(input())
work_days = 365 - free_days
total_play_time = work_days * 63 + free_days * 127
norm = 30000
difference = abs(norm - total_play_time)
hours = difference // 60
minutes = difference % 60
if total_play_time > norm:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
