number = int(input())
left_sum = 0
for i in range(number):
    current_number = int(input())
    left_sum += current_number
right_sum = 0
for i in range(number):
    current_number = int(input())
    right_sum += current_number
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')
