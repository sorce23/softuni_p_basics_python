days = int(input())
type_room = input()
rate = input()
total_sum = 0
nights = days - 1

if type_room == 'room for one person':
    total_sum = nights * 18.00
elif type_room == 'apartment':
    total_sum = nights * 25.00
    if days < 10:
        total_sum *= 0.7
    elif days <= 15:
        total_sum *= 0.65
    else:
        total_sum *= 0.5
elif type_room == 'president apartment':
    total_sum = nights * 35.00
    if days < 10:
        total_sum *= 0.9
    elif days <= 15:
        total_sum *= 0.85
    else:
        total_sum *= 0.8
if rate == 'negative':
    total_sum *= 0.9
elif rate == 'positive':
    total_sum += total_sum * 0.25
print(f'{total_sum:.2f}')
