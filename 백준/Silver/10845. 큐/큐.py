import sys

input = sys.stdin.readline

queue = []
n = int(input())

for _ in range(n):
    a = input().split()

    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        print(queue.pop(0) if queue else -1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        print(0 if queue else 1)
    elif a[0] == 'front':
        print(queue[0] if queue else -1)
    elif a[0] == 'back':
        print(queue[-1] if queue else -1)