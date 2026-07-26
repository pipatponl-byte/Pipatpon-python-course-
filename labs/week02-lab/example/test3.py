
print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()


second = int(input("Enter your seconds: "))
hour = second // 3600
second_remain = second % 3600
minute = second // 60
second_remin = second % 60

print(second,"seconds =",hour,"hour",minute,"minute",second_remain,"second")

