price_vegetables = float(input())
price_fruits = float(input())
vegetables = int(input())
fruits = int(input())
euro = 1.94
total_sum = vegetables * price_vegetables + fruits * price_fruits
total_sum_euro = total_sum / 1.94
print(f'{total_sum_euro:.2f}')
