flowers = input()
number_of_flowers = int(input())
budget = int(input())
price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolus = 2.50
total_sum = 0
if flowers == 'Roses':
    total_sum = number_of_flowers * price_roses
    if number_of_flowers > 80:
        total_sum *= 0.9
elif flowers == 'Dahlias':
    total_sum = number_of_flowers * price_dahlias
    if number_of_flowers > 90:
        total_sum *= 0.85
elif flowers == 'Tulips':
    total_sum = number_of_flowers * price_tulips
    if number_of_flowers > 80:
        total_sum *= 0.85
elif flowers == 'Narcissus':
    total_sum = number_of_flowers * price_narcissus
    if number_of_flowers < 120:
        total_sum += total_sum * 0.15
elif flowers == 'Gladiolus':
    total_sum = number_of_flowers * price_gladiolus
    if number_of_flowers < 80:
        total_sum += total_sum * 0.20
difference = abs(budget - total_sum)
if total_sum <= budget:
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
