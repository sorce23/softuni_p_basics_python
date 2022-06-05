budget = float(input())
numbers_vc = int(input())
numbers_cpu = int(input())
numbers_ram = int(input())
price_vc = 250
sum_vc = numbers_vc * price_vc
price_cpu = sum_vc * 0.35
sum_cpu = numbers_cpu * price_cpu
price_ram = sum_vc * 0.10
sum_ram = numbers_ram * price_ram
total_sum = sum_vc + sum_cpu + sum_ram
if numbers_vc > numbers_cpu:
    total_sum *= 0.85
difference = abs(budget - total_sum)
if total_sum <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
