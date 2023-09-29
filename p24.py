number = 1
i = 0
while number < 10:
    i += 1
    zarb = number * i
    print(number, " * ", i, "=", zarb)
    if i == 10:
        i = 0
        number += 1
