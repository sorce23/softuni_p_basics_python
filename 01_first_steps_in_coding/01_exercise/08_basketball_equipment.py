annual_tax = int(input())
price_baskets = annual_tax * 0.6
price_equip = price_baskets * 0.8
price_ball = price_equip * 0.25
price_accessories = price_ball * 0.2
final_sum = annual_tax + price_baskets + price_equip + \
    price_ball + price_accessories
print(final_sum)
