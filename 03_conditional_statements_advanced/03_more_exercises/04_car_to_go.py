budget = float(input())
season = input()
car_type = ''
car_class = ''
price = 0
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.8
else:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    price = budget * 0.9
print(car_class)
print(f'{car_type} - {price:.2f}')
