number = int(input("your number: "))
zarb = int(input("your zarb: "))
zarb += 1


for i in range(1, zarb):
    javab = number * i
    print(number, "*", i, "=", javab)
