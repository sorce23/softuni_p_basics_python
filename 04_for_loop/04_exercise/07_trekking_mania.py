groups = int(input())
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_tourists = 0
for count in range(groups):
    tourists = int(input())
    total_tourists += tourists
    if 0 < tourists <= 5:
        musala += tourists
    elif 5 < tourists <= 12:
        montblanc += tourists
    elif 12 < tourists <= 25:
        kilimanjaro += tourists
    elif 25 < tourists <= 40:
        k2 += tourists
    elif tourists >= 41:
        everest += tourists
print(f'{(musala / total_tourists) * 100:.2f}%')
print(f'{(montblanc/ total_tourists) * 100:.2f}%')
print(f'{(kilimanjaro / total_tourists) * 100:.2f}%')
print(f'{(k2 / total_tourists) * 100:.2f}%')
print(f'{(everest / total_tourists) * 100:.2f}%')
