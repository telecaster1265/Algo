n, m = map(int, input().split())
b = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    b[i - 1:j] = b[i - 1:j][::-1]

print(*b)