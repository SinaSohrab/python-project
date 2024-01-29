number = int(input("inter your number: "))
number += 1
sum = 0

for i in range(1, number):
    your_number = ("number: ")

    if your_number != i:
        print("loser")
        break

    sum += 1
    print("sum: ", sum)

    if sum % 5 == 0:
        print("sum")

    if i % 5 == 0:
        print("i")
