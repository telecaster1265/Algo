import sys

input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(p)])

    count = 0
    while queue:
        current = queue.popleft()
        if any(current[1] < other[1] for other in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break