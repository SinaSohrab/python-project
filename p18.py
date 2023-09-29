number = 5


def is_prim(n):
    for i in range(1, n):
        if n % number == 0:
            return True
    return False


for i in range(1, 100):
    if is_prim(i):
        print(i)
