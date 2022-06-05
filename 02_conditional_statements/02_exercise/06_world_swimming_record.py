record = float(input())
distance = float(input())
time_per_meter = float(input())
slowdown = (distance // 15) * 12.5
attempt = distance * time_per_meter + slowdown
difference = abs(attempt - record)
if attempt < record:
    print(f'Yes, he succeeded! The new world record is {attempt:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
