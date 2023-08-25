import random

random.seed()

a = []

for i in range(6):
    n = 1
    while random.randint(1, 6) != 6:
        n += 1
        a.append(n)

print(sum(a) / len(a))
