budget = float(input())
season = input()
destination = ''
location = ''
price = 0
if budget <= 1000:
    location = 'Camp'
    if season == 'Summer':
        destination = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        destination = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    location = 'Hut'
    if season == 'Summer':
        destination = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        destination = 'Morocco'
        price = budget * 0.6
else:
    location = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        destination = 'Alaska'
    elif season == 'Winter':
        destination = 'Morocco'
print(f'{destination} - {location} - {price:.2f}')
