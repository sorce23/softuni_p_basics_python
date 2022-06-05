height_house = float(input())
length_house = float(input())
height_roof = float(input())
side_walls = 2 * (height_house * length_house - 1.5 * 1.5)
front_walls = height_house * height_house + (height_house * height_house - 1.2 * 2)
green_paint = (side_walls + front_walls) / 3.4
rooftop = 2 * (height_house * length_house)
rooftop_triangles = 2 * ((height_house * height_roof) / 2)
red_paint = (rooftop + rooftop_triangles) / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
