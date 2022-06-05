stadium_capacity = int(input())
number_fans = int(input())
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0
all_fans = 0
for count in range(number_fans):
    sector = input()
    if sector == 'A':
        sector_A += 1
    elif sector == 'B':
        sector_B += 1
    elif sector == 'V':
        sector_V += 1
    elif sector == 'G':
        sector_G += 1
sector_A = (sector_A / number_fans) * 100
sector_B = (sector_B / number_fans) * 100
sector_V = (sector_V / number_fans) * 100
sector_G = (sector_G / number_fans) * 100
all_fans = (number_fans / stadium_capacity) * 100
print(f'{sector_A:.2f}%')
print(f'{sector_B:.2f}%')
print(f'{sector_V:.2f}%')
print(f'{sector_G:.2f}%')
print(f'{all_fans:.2f}%')
