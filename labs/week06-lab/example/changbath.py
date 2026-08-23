def covert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"(value)  THB = {result} USD")
    else:
        result = value * 33.0
        print(f"(value)  USD = {result} THB")

print(covert_currency(100,"USD"))
print(covert_currency(100, "THB"))