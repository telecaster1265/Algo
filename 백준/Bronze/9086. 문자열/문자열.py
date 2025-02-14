t = int(input())
result = []

for _ in range(t):
    s = input().strip()
    result.append(s[0] + s[-1])

for i in result:
    print(i)
