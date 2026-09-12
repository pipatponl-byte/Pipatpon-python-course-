
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letter 'char' found in '{text}'")


print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  # True
print("'at' not in 'battle':", 'at' not in 'battle')  # False

