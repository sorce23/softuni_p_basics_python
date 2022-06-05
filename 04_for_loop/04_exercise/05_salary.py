tabs_open = int(input())
salary = float(input())
for count in range(1, tabs_open + 1):
    web = input()
    if web == 'Facebook':
        salary -= 150
    elif web == 'Instagram':
        salary -= 100
    elif web == 'Reddit':
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print('You have lost your salary.')
else:
    print(round(salary))
