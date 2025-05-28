import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
card_cnt = list(map(int, input().split()))

cnt = {}

for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

result = []
for num in card_cnt:
    result.append(str(cnt.get(num, 0)))

print(*result, sep=" ")