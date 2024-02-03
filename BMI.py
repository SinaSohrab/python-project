height = float(input("input your height: for cm: "))
weight = float(input("input your weight: for k: "))
#tabdil sc be m
height /= 100
# 1,   argoman round ro 1 adad ashar ro barmogardone
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
