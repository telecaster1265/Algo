import sys

input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    a = input().split()
    if a[0] == '1':
        stack.append(int(a[1]))
    elif a[0] == '2':
        print(stack.pop() if stack else -1)
    elif a[0] == '3':
        print(len(stack))
    elif a[0] == '4':
        print(0 if stack else 1)
    elif a[0] == '5':
        print(stack[-1] if stack else -1)