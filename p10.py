numbers = int(input("your number: "))


def is_prime(n):
    for i in range(0, n):
        if n % 3 == 0 or n % 5 == 0:
            return True
    return False


sum = 0
for i in range(0, numbers):
    if is_prime(i):
        sum = i + sum
print(sum)
