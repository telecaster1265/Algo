n, m = map(int, input().split())
b = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    b[i - 1], b[j - 1] = b[j - 1], b[i - 1]
print(*b)