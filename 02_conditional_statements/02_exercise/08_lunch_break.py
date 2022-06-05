import math

series_name = input()
series_length = int(input())
break_length = int(input())
lunch_time = break_length * 1/8
break_time = break_length * 1/4
time_left = break_length - lunch_time - break_time
difference = abs(time_left - series_length)
if time_left >= series_length:
    print(f'You have enough time to watch {series_name} and left with {math.ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(difference)} more minutes.")
