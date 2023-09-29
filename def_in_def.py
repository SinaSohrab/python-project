def number(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, 1000000):
    if number(i):
        numberr = i
print(numberr)

#fail