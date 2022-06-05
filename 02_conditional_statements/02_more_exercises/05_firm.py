import math

hours_needed = int(input())
days = int(input())
workers = int(input())
total_work_time = (days * 0.9) * 8 + workers * (days * 2)
difference = abs(hours_needed - total_work_time)
if total_work_time > hours_needed:
    print(f'Yes!{math.floor(difference)} hours left.')
else:
    print(f'Not enough time!{math.floor(difference)} hours needed.')
