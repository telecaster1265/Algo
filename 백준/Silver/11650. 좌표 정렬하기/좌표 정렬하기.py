import sys

input = sys.stdin.readline

n = int(input())
dot = []

for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))
dot.sort()

for x, y in dot:
    print(x, y)