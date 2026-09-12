# เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
# password ที่แข็งแรง และยาวมากว่า8 ตัว และผสมกันระหว่าตัวเลข ตัวอักษร และอักขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
# Your password is not storng


password = input("Insert your password: ")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is storng! ")
else:
    print("Your password is not strong! ")
