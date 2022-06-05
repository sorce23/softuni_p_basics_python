money_needed = float(input())
money = float(input())
days_spending = 0
days = 0
while money < money_needed:
    action = input()
    sum_per_day = float(input())
    days += 1
    if action == 'save':
        money += sum_per_day
        days_spending = 0
    elif action == 'spend':
        money -= sum_per_day
        days_spending += 1
    if money < 0:
        money = 0
    if days_spending > 4:
        break
if money >= money_needed:
    print(f'You saved the money for {days} days.')
else:
    print("You can't save the money.")
    print(days)
