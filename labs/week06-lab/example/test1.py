#example1
# Example 1: Simple function without parameters


def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}? Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()


#example3
# Example 3: Mathematical function


def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


#past3
#Example 1: Function that returns a value


def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 5)
sum2 = add_numbers(10, 5)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

# Example 2: Function returning multiple values การคำนวณหาวงกลม


def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volum =  4.0 / 3 * pi * radius **3
    return area, circumference, volum

print("Circle calculations:")
radius = 5
area, circumference, volum = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Volum: {volum:.2f}")
print()

#part4
# Example 1: Function with default parameter


def greet_with_title(name, title="Mr./Ms."):  #ทักทายด้วยคำนำหน้าชื่อ
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

# Example 2: Multiple default parameters


def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults     #ไม่รู้อายุ
create_profile("Bob", 25)  # Age specified  #ไม่รู้ที่อยู่
create_profile("Charlie", 30, "USA")  # All specified
print()

