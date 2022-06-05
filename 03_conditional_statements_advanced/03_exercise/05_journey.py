budget = float(input())
season = input()
destination = ''
location = ''
total_sum = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        location = 'Camp'
        total_sum = budget * 0.3
    elif season == 'winter':
        location = 'Hotel'
        total_sum = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        location = 'Camp'
        total_sum = budget * 0.4
    elif season == 'winter':
        location = 'Hotel'
        total_sum = budget * 0.8
else:
    destination = 'Europe'
    location = 'Hotel'
    total_sum = budget * 0.9
print(f'Somewhere in {destination}')
print(f'{location} - {total_sum:.2f}')
