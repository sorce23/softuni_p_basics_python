distance = int(input())
daytime = input()
price_taxi_day = 0.79
price_taxi_night = 0.90
price_taxi_start = 0.70
price_bus = 0.09# min 20km
price_train = 0.06#min 100km
total_sum = 0
if distance < 20:
    if daytime == 'day':
        total_sum = distance * price_taxi_day + price_taxi_start
    else:
        total_sum = distance * price_taxi_night + price_taxi_start
elif distance < 100:
    total_sum = distance * price_bus
else:
    total_sum = distance * price_train
print(f'{total_sum:.2f}')
