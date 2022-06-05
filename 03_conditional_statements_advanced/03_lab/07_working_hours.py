time = int(input())
day = input()
if day != 'Saturday' and day != 'Sunday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')
