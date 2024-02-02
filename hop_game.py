number = int(input("inter your number: "))
number += 1
sum = 0

for i in range(1, number):
    sum+=1
    
    
    your_number = int(input("number: "))

    if your_number != i:
        print("loser")
        break


    if i % 5 == 0:
        print("i")
