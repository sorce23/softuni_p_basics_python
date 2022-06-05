months = int(input())
bill_electricity = 0
bill_water = 0
bill_internet = 0
bill_others = 0
total_el = 0
total_water = 0
total_internet = 0
total_others = 0
for count in range(months):
    bill_electricity = float(input())
    bill_water = 20
    bill_internet = 15
    bill_all = bill_electricity + bill_water + bill_internet
    bill_others = bill_all + bill_all * 0.2
    total_el += bill_electricity
    total_water += bill_water
    total_internet += bill_internet
    total_others += bill_others
average = (total_el + total_water + total_internet + total_others) / months
print(f'Electricity: {total_el:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Others: {total_others:.2f} lv')
print(f'Average: {average:.2f} lv')
