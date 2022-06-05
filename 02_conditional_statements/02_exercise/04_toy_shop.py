excursion_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddies = int(input())
number_minions = int(input())
number_trucks = int(input())
price_puzzle = 2.60
price_doll = 3
price_teddie = 4.10
price_minion = 8.20
price_truck = 2
total_sum = number_puzzles * price_puzzle + \
    number_dolls * price_doll + number_teddies * price_teddie + \
    number_minions * price_minion + number_trucks * price_truck
total_count = number_puzzles + number_dolls + number_teddies + \
    number_minions + number_trucks
if total_count >= 50:
    total_sum *= 0.75
money_left = total_sum * 0.9
difference = abs(money_left - excursion_price)
if money_left >= excursion_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
