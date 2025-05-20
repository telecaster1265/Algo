import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pic = []

for _ in range(n):
    pic.append(list(map(int, input().split())))

visit = [[False] * m for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    area = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and pic[nx][ny] == 1:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    return area


cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and not visit[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)