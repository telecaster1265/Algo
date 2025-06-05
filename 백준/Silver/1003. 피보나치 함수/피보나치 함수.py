import sys

input = sys.stdin.readline

t = int(input())

f = [0] * 41
g = [0] * 41

f[0] = 1
g[0] = 0
f[1] = 0
g[1] = 1

for i in range(2, 41):
    f[i] = f[i - 1] + f[i - 2]
    g[i] = g[i - 1] + g[i - 2]

for _ in range(t):
    n = int(input())
    print(f[n], g[n])