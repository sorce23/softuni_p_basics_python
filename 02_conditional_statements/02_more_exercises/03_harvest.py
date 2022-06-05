import math

vineyard = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())
workers = int(input())
vineyard_for_wine = vineyard * 0.4
wine_produced = (vineyard_for_wine * grapes_per_sqm) / 2.5
difference = abs(wine_produced - wine_needed)
wine_for_workers = difference / workers
if wine_produced < wine_needed:
    print(f'It will be a tough winter! More {math.floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(difference)} liters left -> {math.ceil(wine_for_workers)} liters per person. ')
