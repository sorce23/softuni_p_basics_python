age = float(input())
sex = input()
title = ''
if sex == 'm':
    if age < 16:
        title = 'Master'
    else:
        title = 'Mr.'
elif sex == 'f':
    if age < 16:
        title = 'Miss'
    else:
        title = 'Ms.'
print(title)
