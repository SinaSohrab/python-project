import random
from colorama import Fore
import matplotlib.pyplot as plt
import numpy as np


random.random()
number = int(input("your number: "))
while number < 3 or number > 1000000:
    if number < 3:
        print(Fore.RED, ("The number of bay should be greater than 3: "), Fore.RESET)
        print(Fore.GREEN, ("Try again"), Fore.RESET)
        number = int(input("your number: "))

    if number > 1000000:
        print(Fore.RED,("The number of bay should be greater than 1,000,000: "),Fore.RESET,)
        print(Fore.GREEN, ("Try again"), Fore.RESET)
        number = int(input("your number: "))


def is_prim(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and n % 1 == 0:
            return False
    return True


jame = 0
for i in range(2, number):
    if is_prim(i):
        jame = jame + 1
        prime = i

jame += 1

for i in range(1, jame):
    if random.randrange:
        randomm = random.randint(1, prime)
        print(randomm)

print("The number of prime numbers: ", jame)



