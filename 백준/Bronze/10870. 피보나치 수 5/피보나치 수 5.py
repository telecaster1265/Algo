import sys

input = sys.stdin.readline

n = int(input())


def fivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fivo(n - 1) + fivo(n - 2)


print(fivo(n))
