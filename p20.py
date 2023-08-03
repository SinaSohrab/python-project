import random

number = random.randint(1, 99)
print(number)
javab = input("[b], [k], [d]: ")

while number != "d":
    print(number)
    javab = input("[b], [k], [d]: ")
    if javab == "b":
        number = random.randint(number, 99)
    if javab == "k":
        number = random.randint(1, number)
print("wow")
