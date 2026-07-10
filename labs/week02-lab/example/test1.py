print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

#input
redius = float(input("Enter your redius: "))
area = 3.14159 * redius ** 2
circumference = 2 * 3.14159 * redius

print("Area:",area)
print("Circumference",circumference)
