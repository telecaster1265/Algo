import sys

input = sys.stdin.readline

m = int(input())
n = int(input())


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


primes = []

for i in range(m, n + 1):
    if is_prime(i):
        primes.append(i)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)