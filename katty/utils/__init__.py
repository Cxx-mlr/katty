from math import floor, sqrt
from random import randint

def is_prime(number: int) -> bool:
    for d in range(2, floor(sqrt(number)) + 1):
        if number % d == 0:
            return False
    return number > 1

def random_prime(n: int) -> int:
    assert n > 1

    number = randint(n, 2*n)

    while not is_prime(number):
        if number == 2*n:
            number = n
        else:
            number += 1

    return number