budget = float(input())
ticket_category = input()
people = int(input())
ticket_VIP = 499.99
ticket_normal = 249.99
total_sum = 0
transport = 0
if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25
if ticket_category == 'VIP':
    total_sum = people * ticket_VIP
elif ticket_category == 'Normal':
    total_sum = people * ticket_normal
sum_left = budget - transport
difference = abs(sum_left - total_sum)
if total_sum <= sum_left:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
