import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

p = deque(range(1, n + 1))
result = []

while p:
    p.rotate(-(k - 1))
    result.append(p.popleft())

print("<" + ", ".join(map(str, result)) + ">")