age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toys = 0
sum_gift = 0
total_sum = 0
for count in range(1, age + 1):
    if count % 2 != 0:
        toys += 1
    else:
        sum_gift += 10
        total_sum += sum_gift - 1
final_sum = toys * toy_price + total_sum
difference = abs(final_sum - price_washing_machine)
if final_sum >= price_washing_machine:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
