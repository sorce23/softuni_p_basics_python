junior_bikers = int(input())
senior_bikers = int(input())
route = input()
total_bikers = junior_bikers + senior_bikers
total_sum = 0
if route == 'trail':
    total_sum = junior_bikers * 5.50 + senior_bikers * 7
elif route == 'cross-country':
    if total_bikers >= 50:
        total_sum = junior_bikers * (8 * 0.75) + senior_bikers * (9.50 * 0.75)
    else:
        total_sum = junior_bikers * 8 + senior_bikers * 9.50
elif route == 'downhill':
    total_sum = junior_bikers * 12.25 + senior_bikers * 13.75
elif route == 'road':
    total_sum = junior_bikers * 20 + senior_bikers * 21.50
total_sum *= 0.95
print(f'{total_sum:.2f}')
