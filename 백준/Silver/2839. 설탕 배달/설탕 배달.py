import sys

input = sys.stdin.readline

n = int(input())

for i in range(n // 5, -1, -1):
    r = n - (5 * i)
    if r % 3 == 0:
        j = r // 3
        print(i + j)
        break
else:
    print(-1)