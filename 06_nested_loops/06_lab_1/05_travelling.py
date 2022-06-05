saved_money = 0
destination = ''
while destination != 'End':
    destination = input()
    budget = float(input())
    if saved_money >= budget:
        print(f'Going to {destination}!')
    while budget > saved_money:
        money = float(input())
        saved_money += money
