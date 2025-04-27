import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    front = ""
    is_group = True
    cut = []

    for char in word:
        if char != front:
            if char in cut:
                is_group = False
                break
            cut.append(front)
        front = char

    if is_group:
        cnt += 1
print(cnt)
