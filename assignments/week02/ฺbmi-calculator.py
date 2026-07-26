weight = int(input("Enter weight: "))

hight = float(input("Enter hight: "))


BMI = weight / hight ** 2

print("BMI: "+str(BMI))

if BMI < 18.5 :
    print("Underweight")

elif BMI > 18.5:
    print("Normal weight")

elif BMI > 25.0 :
    print("Overweight")

elif BMI > 30.0:
    print("Obese")