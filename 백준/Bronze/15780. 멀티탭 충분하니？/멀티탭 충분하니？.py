n,k = map(int, input().split())
a = list(map(int, input().split()))

plug = sum([(i + 1) // 2 for i in a])

if plug >= n:
    print("YES")
else:
    print("NO")