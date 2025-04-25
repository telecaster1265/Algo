import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)

for i in numbers:
    print(i)