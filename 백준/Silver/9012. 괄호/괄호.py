import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    vps = input().strip()
    stack = []
    is_vps = True

    for char in vps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                is_vps = False
                break
            stack.pop()

    if stack:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")