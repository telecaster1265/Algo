import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hear = set()
see = set()

for _ in range(n):
    hear.add(input().strip())

for _ in range(m):
    name = input().strip()
    if name in hear:
        see.add(name)

answer = sorted(see)
print(len(answer))
for name in answer:
    print(name)