score = []

for i in range(1, 6):
    score.append(int(input(f"Enter score of student {i}: ")))
    

print()

for i in range(len(score)):
    if score [i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    print(f"Student {i + 1}: {score[i]} = {result}")


