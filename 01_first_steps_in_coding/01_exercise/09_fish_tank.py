length = int(input())
width = int(input())
height = int(input())
occupy_percentage = float(input())
aquarium_v = (length * width * height) / 1000
liters_needed = aquarium_v - aquarium_v * occupy_percentage / 100
print(liters_needed)
