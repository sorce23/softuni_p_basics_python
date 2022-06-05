import sys

input_number = int(input())
odd_max_number = -sys.maxsize
even_max_number = -sys.maxsize
odd_min_number = sys.maxsize
even_min_number = sys.maxsize
sum_odd = 0
sum_even = 0
for count in range(1, input_number + 1):
    current_number = float(input())
    if count % 2 != 0:
        sum_odd += current_number
        if current_number > odd_max_number:
            odd_max_number = current_number
        if current_number < odd_min_number:
            odd_min_number = current_number
    else:
        sum_even += current_number
        if current_number > even_max_number:
            even_max_number = current_number
        if current_number < even_min_number:
            even_min_number = current_number
if sum_odd != 0 and sum_even != 0:
    print(f'OddSum={sum_odd:.2f},')
    print(f'OddMin={odd_min_number:.2f},')
    print(f'OddMax={odd_max_number:.2f},')
    print(f'EvenSum={sum_even:.2f},')
    print(f'EvenMin={even_min_number:.2f},')
    print(f'EvenMax={even_max_number:.2f}')
elif sum_odd == 0 and sum_even != 0:
    print(f'OddSum={sum_odd:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={sum_even:.2f},')
    print(f'EvenMin={even_min_number:.2f},')
    print(f'EvenMax={even_max_number:.2f}')
elif sum_odd != 0 and sum_even == 0:
    print(f'OddSum={sum_odd:.2f},')
    print(f'OddMin={odd_min_number:.2f},')
    print(f'OddMax={odd_max_number:.2f},')
    print(f'EvenSum={sum_even:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={sum_odd:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={sum_even:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
