number = int(input("your number: "))
number += 1

first = 1
secend = 1

for i in range(1, number):
    first = i
    zarb = first * secend
    secend = zarb

print(zarb)
