import sys

input = sys.stdin.readline

n = int(input())
dots = []

for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda dot: (dot[1], dot[0]))

for dot in dots:
    print(dot[0], dot[1])