import sys

input = sys.stdin.readline

n = int(input())

def matrix(n):
    line = 1
    sum = 0

    while sum + line < n:
        sum += line
        line += 1

    i = n - sum

    if line % 2 == 0:
        top = i
        bot = line - i + 1
    else:
        top = line - i + 1
        bot = i
    return f"{top}/{bot}"


print(matrix(n))