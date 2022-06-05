fuel = input()
quantity = float(input())
club_card = input()
price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
total_sum = 0
if club_card == 'Yes':
    price_gasoline -= 0.18
    price_diesel -= 0.12
    price_gas -= 0.08
if fuel == 'Diesel':
    total_sum = quantity * price_diesel
elif fuel == 'Gasoline':
    total_sum = quantity * price_gasoline
elif fuel == 'Gas':
    total_sum = quantity * price_gas
if 20 <= quantity <= 25:
    total_sum *= 0.92
elif quantity > 25:
    total_sum *= 0.9
print(f'{total_sum:.2f}')
