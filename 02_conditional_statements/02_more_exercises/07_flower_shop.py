import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
price_gift = float(input())
price_magnolia = 3.25
price_hyacinth = 4
price_rose = 3.50
price_cactus = 8
total_sum = magnolias * price_magnolia + \
    hyacinths * price_hyacinth + \
    roses * price_rose + \
    cactus * price_cactus
total_sum *= 0.95
difference = abs(total_sum - price_gift)
if total_sum >= price_gift:
    print(f'She is left with {math.floor(difference)} leva.')
else:
    print(f'She will have to borrow {math.ceil(difference)} leva.')
