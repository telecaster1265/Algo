n, m = map(int, input().split())
numbers = list(map(int, input().split()))

total = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            s = numbers[i] + numbers[j] + numbers[k]
            if s <= m:
                total = max(total,s)

print(total)