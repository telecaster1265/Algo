import sys


input = sys.stdin.readline

k = int(input())
numbers = []

for _ in range(k):
    a = int(input().strip())
    if a == 0:
        numbers.pop()
    else:
        numbers.append(a)

print(sum(numbers))