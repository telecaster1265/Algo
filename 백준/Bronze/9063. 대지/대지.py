import sys

input = sys.stdin.readline

n = int(input())
x_dots = []
y_dots = []

for _ in range(n):
    x, y = map(int, input().split())
    x_dots.append(x)
    y_dots.append(y)

ex = (max(x_dots) - min(x_dots)) * (max(y_dots) - min(y_dots))
print(ex)