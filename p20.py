import random

a = 1
g = 99
number = random.randint(a, g)
print(number)
javab = input("[b], [k], [d]: ")

while javab != "d":
    print(number)
    javab = input("[b], [k], [d]: ")
    if javab == "b":
        number = random.randint(a, 99)
        a = number
    if javab == "k":
        number = random.randint(1, g)
        g = number

print("wow your number ",number)
