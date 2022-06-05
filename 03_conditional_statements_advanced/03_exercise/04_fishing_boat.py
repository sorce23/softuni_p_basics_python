budget = int(input())
season = input()
fishers = int(input())
price_boat_spring = 3000
price_boat_summer_autumn = 4200
price_boat_winter = 2600
total_sum = 0
if season == 'Spring':
    if 0 < fishers <= 6:
        total_sum = price_boat_spring * 0.9
    elif 7 < fishers <= 11:
        total_sum = price_boat_spring * 0.85
    elif fishers >= 12:
        total_sum = price_boat_spring * 0.75
elif season == 'Summer' or season == 'Autumn':
    if 0 < fishers <= 6:
        total_sum = price_boat_summer_autumn* 0.9
    elif 7 < fishers <= 11:
        total_sum = price_boat_summer_autumn * 0.85
    elif fishers >= 12:
        total_sum = price_boat_summer_autumn * 0.75
elif season == 'Winter':
    if 0 < fishers <= 6:
        total_sum = price_boat_winter * 0.9
    elif 7 < fishers <= 11:
        total_sum = price_boat_winter * 0.85
    elif fishers >= 12:
        total_sum = price_boat_winter * 0.75
if fishers % 2 == 0 and season != 'Autumn':
    total_sum *= 0.95
difference = abs(budget - total_sum)
if total_sum <= budget:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')

# budget = int(input())
# season = input()
# fisherman = int(input())
# rent = 0
# if season == 'Spring':
#     rent = 3000
# elif season == 'Summer' or season == 'Autumn':
#     rent = 4200
# elif season == 'Winter':
#     rent = 2600
# if fisherman <= 6:
#     rent *= 0.9
# elif fisherman <= 11:
#     rent *= 0.85
# else:
#     rent *= 0.75
# if fisherman % 2 == 0 and season != 'Autumn':
#     rent *= 0.95
# diff = abs(rent - budget)
# if rent <= budget:
#     print(f'Yes! You have {diff:.2f} leva left.')
# else:
#     print(f'Not enough money! You need {diff:.2f} leva.')
