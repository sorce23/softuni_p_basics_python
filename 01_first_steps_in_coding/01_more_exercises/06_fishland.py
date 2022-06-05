price_fish_1 = float(input())
price_fish_2 = float(input())
quantity_fish_3 = float(input())
quantity_fish_4 = float(input())
quantity_fish_5 = int(input())
price_fish_3 = price_fish_1 + price_fish_1 * 0.6
price_fish_4 = price_fish_2 + price_fish_2 * 0.8
price_fish_5 = 7.50
total_sum = quantity_fish_3 * price_fish_3 + \
    quantity_fish_4 * price_fish_4 + \
    quantity_fish_5 * price_fish_5
print(f'{total_sum:.2f}')
