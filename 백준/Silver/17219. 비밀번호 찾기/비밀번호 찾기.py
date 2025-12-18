import sys

input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}
for _ in range(n):
    site, password = input().split()
    memo[site] = password

for _ in range(m):
    find = input().strip()
    print(memo[find])