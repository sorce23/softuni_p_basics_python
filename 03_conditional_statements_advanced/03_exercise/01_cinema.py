projection = input()
rows = int(input())
columns = int(input())
ticket = 0
income = 0
if projection == 'Premiere':
    ticket = 12.00
elif projection == 'Normal':
    ticket = 7.50
elif projection == 'Discount':
    ticket = 5.00
income = (rows * columns) * ticket
print(f'{income:.2f} leva')
