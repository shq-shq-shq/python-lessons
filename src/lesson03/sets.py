пятерочники = {"Иван Широков", "Василий Широков"}

primes = {2, 3, 5, 7, 11, 13}

empty_set = {}


def all_divisors(x):
    divisors = set()
    for i in range(2, x + 1):
        if x % i == 0:
            divisors.add(i)
    return divisors

dA = all_divisors(81)
dB = all_divisors(27)

print(max(dA.intersection(dB)))


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

print(gcd(128, 256))