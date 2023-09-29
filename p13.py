number = int(input("your number: "))
Even = []


def Even_number(n):
    for i in range(0, n):
        if n % 2 == 0:
            return True    
    return False


for i in range(0, number):
    if Even_number(i):
        Even.append(i)

print(Even)
