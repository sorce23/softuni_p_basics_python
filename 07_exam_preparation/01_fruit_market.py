price_strawberry = float(input())
quantity_banana = float(input())
quantity_orange = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())
price_raspberry = price_strawberry * 0.5
price_orange = price_raspberry * 0.6
price_banana = price_raspberry * 0.2
total_sum = price_banana * quantity_banana + \
    price_orange * quantity_orange + \
    price_raspberry * quantity_raspberry + \
    price_strawberry * quantity_strawberry
print(f'{total_sum:.2f}')
