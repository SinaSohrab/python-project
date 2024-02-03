height = float(input("input your height: "))
weight = float(input("input your weight: "))
height /= 100
BMI = round(weight / (height * height), 1)

print(f"BMI: {BMI}")

if BMI < 18.5:
    print("kambod vazn.")
elif BMI < 25:
    print("normal.")
elif BMI < 30:
    print("ezafe vazn.")
else:
    print("chaghe.")
