import itertools


def is_simple_number(num):
    if num < 2:
        return False
    divider = 2
    while divider < num:
        if num % divider == 0:
            return False
        divider += 1
    return True


def primes():
    num = 2
    while True:
        if is_simple_number(num):
            yield num
        num += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))

