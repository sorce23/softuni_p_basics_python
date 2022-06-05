season = input()
km_per_month = float(input())
pay_per_km = 0
total_pay = 0
if 0 < km_per_month <= 5000:
    if season == 'Summer':
        pay_per_km = 0.9
    elif season == 'Winter':
        pay_per_km = 1.05
    else:
        pay_per_km = 0.75
elif 5000 < km_per_month <= 10000:
    if season == 'Summer':
        pay_per_km = 1.10
    elif season == 'Winter':
        pay_per_km = 1.25
    else:
        pay_per_km = 0.95
elif 10000 < km_per_month <= 20000:
    pay_per_km = 1.45
total_pay = 4 * (km_per_month * pay_per_km)
total_pay *= 0.9
print(f'{total_pay:.2f}')
