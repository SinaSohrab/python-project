number = int(input("your number: "))


def is_prim(n):
    for i in range(2, int(n)):
        if n % i == 0 and n % 1 == 0:
            return False
    return True


for i in range(2, number):
    if is_prim(i):
        print(i)
