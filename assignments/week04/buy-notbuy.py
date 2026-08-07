
items = []

print("Enter prices of 6 item: ")

for i in range(1, 7):
    items.append(int(input(f"Item {i}: ")))

print()
budget =int(input("Enter total Budget :"))
print()

total = 0
bought = []


for i in range(1, 7):
    price = items[i - 1]
    if total + price <= budget:
        total += price
        bought.append(price)
        print(f"Item {i} = price -> buy")
    else:
        print(f"Item {i} = price -> can not by ")
    print(f"Current total = {total}")
    print()

print(f"Bought items: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget}")

