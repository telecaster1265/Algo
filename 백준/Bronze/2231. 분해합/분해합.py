n = int(input())

for i in range(1, n + 1):
    m = list(map(int, str(i)))
    total = sum(m)
    if i + total == n:
        print(i)
        break
else:
    print(0)