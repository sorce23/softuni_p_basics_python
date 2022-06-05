cargo = int(input())
bus = 0
truck = 0
train = 0
average_sum = 0
for count in range(cargo):
    cargo_weight = int(input())
    if 0 < cargo_weight <= 3:
        average_sum += cargo_weight * 200
        bus += cargo_weight
    elif 4 <= cargo_weight <= 11:
        average_sum += cargo_weight * 175
        truck += cargo_weight
    elif cargo_weight >= 12:
        average_sum += cargo_weight * 120
        train += cargo_weight
total_cargo = bus + truck + train
average_sum = average_sum / total_cargo
bus = bus / total_cargo * 100
truck = truck / total_cargo * 100
train = train / total_cargo * 100
print(f'{average_sum:.2f}')
print(f'{bus:.2f}%')
print(f'{truck:.2f}%')
print(f'{train:.2f}%')
