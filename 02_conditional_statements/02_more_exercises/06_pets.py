import math

number_days = int(input())
food_left = int(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input())
total_food = number_days * food_dog + number_days * food_cat + \
    number_days * (food_turtle / 1000)
difference = abs(total_food - food_left)
if food_left >= total_food:
    print(f'{math.floor(difference)} kilos of food left.')
else:
    print(f'{math.ceil(difference)} more kilos of food are needed.')
