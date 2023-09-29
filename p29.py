i = 0
jam = 0
while True:
    number = float(input("your number: "))
    if number == 0:
        break
    i += 1
    jam = jam + number
print(jam / i)
