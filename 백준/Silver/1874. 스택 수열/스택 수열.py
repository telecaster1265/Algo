import sys

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

stack = []
result = []
current = 1
possible = True

for number in numbers:
    while current <= number:
        stack.append(current)
        result.append("+")
        current += 1

    if stack and stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")