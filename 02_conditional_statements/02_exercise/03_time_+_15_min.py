hour = int(input())
minutes = int(input())
total_minutes = hour * 60 + minutes + 15
hour_from_total = total_minutes // 60
minutes_from_total = total_minutes % 60
if hour_from_total <= 23:
    if minutes_from_total <= 9:
        print(f'{hour_from_total}:0{minutes_from_total}')
    else:
        print(f'{hour_from_total}:{minutes_from_total}')
else:
    if minutes_from_total <= 9:
        print(f'0:0{minutes_from_total}')
    else:
        print(f'0:{minutes_from_total}')
