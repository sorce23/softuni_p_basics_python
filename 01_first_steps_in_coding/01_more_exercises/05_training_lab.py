length = float(input())
width = float(input())
hall_length_cm = length * 100
hall_width_cm = width * 100 - 100
desk_length = 120
desk_width = 70
total_desks = (hall_length_cm // desk_length) * (hall_width_cm // desk_width) - 3
print(round(total_desks))
