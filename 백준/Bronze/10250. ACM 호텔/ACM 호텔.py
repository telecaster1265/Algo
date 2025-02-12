t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y = n % h
    xx = n // h + 1

    if y == 0:
        y = h
        xx -= 1

    print(f"{y}{xx:02d}")