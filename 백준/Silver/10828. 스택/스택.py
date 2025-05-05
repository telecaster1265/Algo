import sys

input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    a = input().split()
    if a[0] == 'push':
        stack.append(int(a[1]))
    elif a[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        print(0 if stack else 1)
    elif a[0] == 'top':
        print(stack[-1] if stack else -1)