number_pens = int(input())
number_markers = int(input())
liters_detergent = int(input())
discount = int(input())
price_pens = 5.80
price_markers = 7.20
price_detergent = 1.20
total_sum = number_pens * price_pens + \
    number_markers * price_markers + \
    liters_detergent * price_detergent
final_sum = total_sum - total_sum * discount / 100
print(final_sum)
