menu_chicken = int(input())
menu_fish = int(input())
menu_veggie = int(input())
price_chicken = 10.35
price_fish = 12.40
price_veggie = 8.15
delivery = 2.50
total_sum_menu = menu_chicken * price_chicken + \
    menu_fish * price_fish + menu_veggie * price_veggie
dessert = total_sum_menu * 0.2
final_sum = total_sum_menu + dessert + delivery
print(final_sum)
