import sys

input = sys.stdin.readline

n, k = map(int, input().split())
div = []

for i in range(1, n+1):
    if n % i == 0:
        div.append(i)

if k <= len(div):
    print(div[k-1])
else:
    print(0)