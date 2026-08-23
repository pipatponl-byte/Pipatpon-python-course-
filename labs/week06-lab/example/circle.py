def calculate_circle_info(radius):

    pi = 3.14159
    area =  pi * radius * radius
    circumference = 2 * pi * radius
    volumn = 4.0 / 3 * pi * radius ** 3
    return area, circumference

print("Calculate circle")
radius = 5
area, circumference = calculate_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

print("3.14159 = ",area)
print()

    