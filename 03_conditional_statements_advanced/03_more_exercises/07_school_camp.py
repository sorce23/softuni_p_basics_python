season = input()
group = input()
number_of_group = int(input())
nights = int(input())
sport = ''
price = 0
total_sum = 0
if season == 'Winter':
    if group == 'mixed':
        price = 10
        sport = 'Ski'
    else:
        price = 9.60
        if group == 'boys':
            sport = 'Judo'
        else:
            sport = 'Gymnastics'
elif season == 'Spring':
    if group == 'mixed':
        price = 9.50
        sport = 'Cycling'
    else:
        price = 7.20
        if group == 'boys':
            sport = 'Tennis'
        else:
            sport = 'Athletics'
elif season == 'Summer':
    if group == 'mixed':
        price = 20
        sport = 'Swimming'
    else:
        price = 15
        if group == 'boys':
            sport = 'Football'
        else:
            sport = 'Volleyball'
total_sum = nights * price * number_of_group
if 20 > number_of_group >= 10:
    total_sum *= 0.95
elif 50 > number_of_group >= 20:
    total_sum *= 0.85
elif number_of_group >= 50:
    total_sum *= 0.5
print(f'{sport} {total_sum:.2f} lv.')
