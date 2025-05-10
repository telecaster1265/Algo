import sys

input = sys.stdin.readline


n, b = map(int, input().split())

conv = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while n > 0:
    result = conv[n % b] + result
    n //= b

print(result)