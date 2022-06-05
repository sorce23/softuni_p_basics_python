number = int(input())
sum_even = 0
sum_odd = 0
for count in range(1, number + 1):
    current_number = int(input())
    if count % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number
if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    difference = abs(sum_even - sum_odd)
    print('No')
    print(f'Diff = {difference}')
