number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
total_flowers = number_roses + number_tulips + number_chrysanthemums
total_sum = 0
if season == 'Spring' or season == 'Summer':
    total_sum = number_chrysanthemums * 2.00 + number_roses * 4.10 + number_tulips * 2.50
elif season == 'Autumn' or season == 'Winter':
    total_sum = number_chrysanthemums * 3.75 + number_roses * 4.50 + number_tulips * 4.15
if holiday == 'Y':
    total_sum += total_sum * 0.15
if season == 'Spring' and number_tulips > 7:
    total_sum *= 0.95
if season == 'Winter' and number_roses >= 10:
    total_sum *= 0.9
if total_flowers > 20:
    total_sum *= 0.8
final_sum = total_sum + 2
print(f'{final_sum:.2f}')
