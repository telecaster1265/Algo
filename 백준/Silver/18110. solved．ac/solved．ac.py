import sys
input = sys.stdin.readline

def round_up(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)

n = int(input())
if n == 0:
    print(0)
else:
    level = [int(input()) for _ in range(n)]
    cut = round_up(n * 0.15)
    level.sort()
    cutting = level[cut: n - cut]
    average = round_up(sum(cutting) / len(cutting))
    print(average)
