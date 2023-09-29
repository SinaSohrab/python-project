number = 1000000


def is_prim(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and n % 1 == 0:
            return False
    return True


sum = 0

for i in range(2, number):
    if is_prim(i):
        sum += i

print(sum)
