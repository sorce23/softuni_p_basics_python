x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
if (x == x1 or x == x2) and (y2 >= y >= y1):
    print('Border')
elif (y == y1 or y == y2) and (x1 <= x <= x2):
    print('Border')
else:
    print('Inside / Outside')
